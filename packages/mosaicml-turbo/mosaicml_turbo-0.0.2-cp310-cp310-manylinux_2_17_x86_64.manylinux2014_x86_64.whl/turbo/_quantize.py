from typing import Optional

import torch

import _turbo_kernels as kernels

from ._utils import div_round_up, num_blocks_to_use

_GROUP_SIZE = 32
_BLOCK_SIZE = 128
_scales_dtype = torch.float16


def _check_quantize_inputs(x_f: torch.Tensor, scales: torch.Tensor,
                           x_q: torch.Tensor) -> None:
    # device and layout checks
    for name, tensor in [('x_not_quantized', x_f), ('scales', scales),
                         ('x_quantized', x_q)]:
        if not tensor.is_cuda:
            raise NotImplementedError('Quantization only supported for CUDA ' +
                                      f'tensors. {name} device={tensor.device}')
        if tensor.device != x_f.device:
            raise ValueError(f'{name} device {tensor.device} != ' +
                             f'input device {x_f.device}')
        if not tensor.is_contiguous():
            raise ValueError(f'{name} is not contiguous')

    # dtype checks
    if x_f.dtype not in (torch.float16, torch.bfloat16, torch.float32):
        raise NotImplementedError(
            'Only [de]quantization of float16, bfloat16, and float32 ' +
            f'are supported; got {x_f.dtype}')
    if scales.dtype != torch.float16:
        raise NotImplementedError(f'Scales must be float16, not {scales.dtype}')
    if x_q.dtype != torch.int8:
        raise ValueError(f'Quantized tensor must be int8, not {x_q.dtype}')


def quantize8b(x: torch.Tensor,
               scales_out: Optional[torch.Tensor] = None,
               x_q_out: Optional[torch.Tensor] = None):
    input_size = x.numel()
    if x_q_out is None:
        x_q_out = torch.empty(x.shape, dtype=torch.int8, device=x.device)
    if scales_out is None:
        scales_out = torch.empty(div_round_up(input_size, _GROUP_SIZE),
                                 dtype=_scales_dtype,
                                 device=x.device)
    _check_quantize_inputs(x, scales_out, x_q_out)

    grid_size = num_blocks_to_use(input_size, _BLOCK_SIZE)
    kernels.quantize8b(x, scales_out, x_q_out, grid_size, _BLOCK_SIZE)

    return x_q_out, scales_out


def dequantize8b(x_q: torch.Tensor,
                 scales: torch.Tensor,
                 x_out: Optional[torch.Tensor] = None,
                 out_dtype: torch.dtype = torch.float32) -> torch.Tensor:
    input_size = x_q.numel()
    if x_out is None:
        x_out = torch.empty(x_q.shape, dtype=out_dtype, device=x_q.device)
    _check_quantize_inputs(x_out, scales, x_q)

    grid_size = num_blocks_to_use(input_size, _BLOCK_SIZE)
    kernels.dequantize8b(x_q, scales, x_out, grid_size, _BLOCK_SIZE)

    return x_out
