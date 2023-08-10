# -*- coding: utf-8 -*-

__all__ = (
    "BatchNormSpec",
    "InstanceNormSpec",
    "BatchInstanceNormSpec",
    "GroupNormSpec",
    "LayerNormSpec",
)


from kaparoo_lightning.nn.specs.module import ModuleSpec


class NormSpec(ModuleSpec, total=False):
    eps: float  # 0.00001


class BatchInstanceNormSpec(NormSpec, total=False):
    momentum: float  # = 0.1
    affine: bool  # = True
    track_running_stats: bool  # = True


BatchNormSpec = BatchInstanceNormSpec
InstanceNormSpec = BatchInstanceNormSpec


class GroupNormSpec(NormSpec, total=False):
    affine: bool  # = True


class LayerNormSpec(NormSpec, total=False):
    elementwise_affine: bool  # = True
