# -*- coding: utf-8 -*-

__all__ = (
    "Conv1dSpec",
    "Conv2dSpec",
    "Conv3dSpec",
    "ConvTranspose1dSpec",
    "ConvTranspose2dSpec",
    "ConvTranspose3dSpec",
)


from torch.nn.common_types import _size_1_t, _size_2_t, _size_3_t
from typing_extensions import Required

from kaparoo_lightning.nn.specs.module import ModuleSpec


class ConvNdSpec(ModuleSpec, total=False):
    groups: int  # = 1
    bias: bool  # = True
    padding_mode: str  # = "zeros"


class Conv1dSpec(ConvNdSpec, total=False):
    kernel_size: Required[_size_1_t]
    stride: _size_1_t  # = 1
    padding: str | _size_1_t  # = 0
    dilation: _size_1_t  # = 1


class Conv2dSpec(ConvNdSpec, total=False):
    kernel_size: Required[_size_2_t]
    stride: _size_2_t  # = 1,
    padding: str | _size_2_t  # = 0,
    dilation: _size_2_t  # = 1,


class Conv3dSpec(ConvNdSpec, total=False):
    kernel_size: Required[_size_3_t]
    stride: _size_3_t  # = 1,
    padding: str | _size_3_t  # = 0,
    dilation: _size_3_t  # = 1,


class ConvTransposeNdSpec(ConvNdSpec, total=False):
    pass


class ConvTranspose1dSpec(ConvTransposeNdSpec, total=False):
    kernel_size: Required[_size_1_t]
    stride: _size_1_t  # = 1
    padding: _size_1_t  # = 0
    output_padding: _size_1_t  # = 0
    dilation: _size_1_t  # = 1


class ConvTranspose2dSpec(ConvTransposeNdSpec, total=False):
    kernel_size: Required[_size_2_t]
    stride: _size_2_t  # = 1
    padding: _size_2_t  # = 0
    output_padding: _size_2_t  # = 0
    dilation: _size_2_t  # = 1


class ConvTranspose3dSpec(ConvTransposeNdSpec, total=False):
    kernel_size: Required[_size_3_t]
    stride: _size_3_t  # = 1
    padding: _size_3_t  # = 0
    output_padding: _size_3_t  # = 0
    dilation: _size_3_t  # = 1
