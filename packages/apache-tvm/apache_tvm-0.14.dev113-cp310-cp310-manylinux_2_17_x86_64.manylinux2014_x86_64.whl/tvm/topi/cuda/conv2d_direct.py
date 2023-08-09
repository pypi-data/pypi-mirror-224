# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
# pylint: disable=invalid-name
"""The templates for cuda conv2d operators"""
import tvm
from tvm import te
from tvm import autotvm
from ..utils import get_const_tuple


def schedule_direct_cuda(cfg, s, conv):
    """schedule optimized for batch size = 1"""

    ##### space definition begin #####
    n, f, y, x = s[conv].op.axis
    rc, ry, rx = s[conv].op.reduce_axis
    cfg.define_split("tile_f", f, num_outputs=4)
    cfg.define_split("tile_y", y, num_outputs=4)
    cfg.define_split("tile_x", x, num_outputs=4)
    cfg.define_split("tile_rc", rc, num_outputs=2)
    cfg.define_split("tile_ry", ry, num_outputs=2)
    cfg.define_split("tile_rx", rx, num_outputs=2)
    cfg.define_knob("auto_unroll_max_step", [0, 512, 1500])

    target = tvm.target.Target.current()
    if target.kind.name in ["nvptx", "rocm"]:
        cfg.define_knob("unroll_explicit", [1])
    else:
        cfg.define_knob("unroll_explicit", [0, 1])

    # fallback support
    if cfg.is_fallback:
        ref_log = autotvm.tophub.load_reference_log(
            target.kind.name, target.model, "conv2d_nchw.cuda"
        )
        cfg.fallback_with_reference_log(ref_log)
    ##### space definition end #####

    pad_data, kernel = s[conv].op.input_tensors

    s[pad_data].compute_inline()
    if isinstance(kernel.op, tvm.te.ComputeOp) and "dilate" in kernel.op.tag:
        s[kernel].compute_inline()

    if conv.op in s.outputs:
        output = conv
        OL = s.cache_write(conv, "local")
    else:
        output = s.outputs[0].output(0)
        s[conv].set_scope("local")
        OL = conv

    # create cache stage
    AA = s.cache_read(pad_data, "shared", [OL])
    WW = s.cache_read(kernel, "shared", [OL])

    # tile and bind spatial axes
    n, f, y, x = s[output].op.axis
    kernel_scope, n = s[output].split(n, nparts=1)

    bf, vf, tf, fi = cfg["tile_f"].apply(s, output, f)
    by, vy, ty, yi = cfg["tile_y"].apply(s, output, y)
    bx, vx, tx, xi = cfg["tile_x"].apply(s, output, x)

    bf = s[output].fuse(n, bf)
    s[output].bind(bf, te.thread_axis("blockIdx.z"))
    s[output].bind(by, te.thread_axis("blockIdx.y"))
    s[output].bind(bx, te.thread_axis("blockIdx.x"))
    s[output].bind(vf, te.thread_axis("vthread"))
    s[output].bind(vy, te.thread_axis("vthread"))
    s[output].bind(vx, te.thread_axis("vthread"))
    s[output].bind(tf, te.thread_axis("threadIdx.z"))
    s[output].bind(ty, te.thread_axis("threadIdx.y"))
    s[output].bind(tx, te.thread_axis("threadIdx.x"))
    s[output].reorder(bf, by, bx, vf, vy, vx, tf, ty, tx, fi, yi, xi)
    s[OL].compute_at(s[output], tx)

    # tile reduction axes
    n, f, y, x = s[OL].op.axis
    rc, ry, rx = s[OL].op.reduce_axis
    rco, rci = cfg["tile_rc"].apply(s, OL, rc)
    ryo, ryi = cfg["tile_ry"].apply(s, OL, ry)
    rxo, rxi = cfg["tile_rx"].apply(s, OL, rx)
    s[OL].reorder(rco, ryo, rxo, rci, ryi, rxi, n, f, y, x)

    s[AA].compute_at(s[OL], rxo)
    s[WW].compute_at(s[OL], rxo)

    # cooperative fetching
    for load in [AA, WW]:
        n, f, y, x = s[load].op.axis
        fused = s[load].fuse(n, f, y, x)
        tz, fused = s[load].split(fused, nparts=cfg["tile_f"].size[2])
        ty, fused = s[load].split(fused, nparts=cfg["tile_y"].size[2])
        tx, fused = s[load].split(fused, nparts=cfg["tile_x"].size[2])
        s[load].bind(tz, te.thread_axis("threadIdx.z"))
        s[load].bind(ty, te.thread_axis("threadIdx.y"))
        s[load].bind(tx, te.thread_axis("threadIdx.x"))

    # unroll
    s[output].pragma(kernel_scope, "auto_unroll_max_step", cfg["auto_unroll_max_step"].val)
    s[output].pragma(kernel_scope, "unroll_explicit", cfg["unroll_explicit"].val)

    N, CO, OH, OW = get_const_tuple(output.shape)
    _, KH, KW, CI = get_const_tuple(kernel.shape)

    if isinstance(N, int):
        cfg.add_flop(2 * N * OH * OW * CO * CI * KH * KW)
