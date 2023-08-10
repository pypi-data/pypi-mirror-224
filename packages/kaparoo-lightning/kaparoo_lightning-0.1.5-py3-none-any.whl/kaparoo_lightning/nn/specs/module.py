# -*- coding: utf-8 -*-

__all__ = ("ModuleSpec",)

from typing import Any

from kaparoo_lightning.common.spec import SpecBase


class ModuleSpec(SpecBase, total=False):
    device: Any | None
    dtype: Any | None
