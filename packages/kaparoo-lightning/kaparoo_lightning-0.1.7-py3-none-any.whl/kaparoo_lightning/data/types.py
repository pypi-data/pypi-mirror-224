# -*- coding: utf-8 -*-

__all__ = ("DoubleDomainTransform", "MultiDomainTransform")

from collections.abc import Sequence
from typing import TypeAlias

from kaparoo.utils.types import T_co

from kaparoo_lightning.common.types import TensorFn

DoubleDomainTransform: TypeAlias = (
    TensorFn[T_co] | tuple[TensorFn[T_co] | None, TensorFn[T_co] | None]
)
MultiDomainTransform: TypeAlias = TensorFn[T_co] | Sequence[TensorFn[T_co] | None]
