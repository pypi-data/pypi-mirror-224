# -*- coding: utf-8 -*-

from __future__ import annotations

__all__ = ("ResidualBlock",)

from abc import abstractmethod
from typing import TYPE_CHECKING

import torch.nn as nn

if TYPE_CHECKING:
    from torch import Tensor


class ResidualBlock(nn.Module):
    @abstractmethod
    def residual(self, x: Tensor) -> Tensor:
        raise NotImplementedError

    def shortcut(self, x: Tensor) -> Tensor:
        return x

    def forward(self, x: Tensor) -> Tensor:
        return self.residual(x) + self.shortcut(x)
