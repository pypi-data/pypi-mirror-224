# -*- coding: utf-8 -*-

__all__ = (
    # base
    "ModuleSpec",
    # convolution
    "Conv1dSpec",
    "Conv2dSpec",
    "Conv3dSpec",
    "ConvTranspose1dSpec",
    "ConvTranspose2dSpec",
    "ConvTranspose3dSpec",
    # normalization
    "BatchInstanceNormSpec",
    "BatchNormSpec",
    "InstanceNormSpec",
    "GroupNormSpec",
    "LayerNormSpec",
)

from kaparoo_lightning.nn.specs.conv import (
    Conv1dSpec,
    Conv2dSpec,
    Conv3dSpec,
    ConvTranspose1dSpec,
    ConvTranspose2dSpec,
    ConvTranspose3dSpec,
)
from kaparoo_lightning.nn.specs.module import ModuleSpec
from kaparoo_lightning.nn.specs.norm import (
    BatchInstanceNormSpec,
    BatchNormSpec,
    GroupNormSpec,
    InstanceNormSpec,
    LayerNormSpec,
)
