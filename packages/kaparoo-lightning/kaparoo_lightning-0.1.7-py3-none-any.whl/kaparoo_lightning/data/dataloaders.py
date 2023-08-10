# -*- coding: utf-8 -*-

from __future__ import annotations

__all__ = ("DataLoaderSpec",)

from collections.abc import Iterable, Sequence
from typing import TYPE_CHECKING

from kaparoo_lightning.common.spec import SpecBase

if TYPE_CHECKING:
    from typing import Any

    from torch.utils.data import Sampler
    from torch.utils.data.dataloader import _collate_fn_t, _worker_init_fn_t


class DataLoaderSpec(SpecBase, total=False):
    batch_size: int | None  # = 1
    shuffle: bool | None  # = None
    sampler: Sampler | Iterable | None  # = None
    batch_sampler: Sampler[Sequence] | Iterable[Sequence] | None  # = None
    num_workers: int  # = 0
    collate_fn: _collate_fn_t | None  # = None
    pin_memory: bool  # = False
    drop_last: bool  # = False
    timeout: float  # = 0
    worker_init_fn: _worker_init_fn_t | None  # = None
    multiprocessing_context: Any | None  # = None
    generator: Any | None  # = None
    prefetch_factor: int | None  # = None
    persistent_workers: bool  # = False
    pin_memory_device: str  # = ""
