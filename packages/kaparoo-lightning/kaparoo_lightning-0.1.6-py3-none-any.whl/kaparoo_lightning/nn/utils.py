# -*- coding: utf-8 -*-

__all__ = ("make_exponential_list",)

from kaparoo.utils.optional import replace_if_none


def make_exponential_list(
    length: int,
    scale: int = 1,
    offset: int = 0,
    base: int = 2,
    min_: int | None = None,
    max_: int | None = None,
) -> list[int]:
    min_ = replace_if_none(min_, float("-inf"))
    max_ = replace_if_none(max_, float("+inf"))
    if min_ > max_:
        min_, max_ = max_, min_

    return [min(max(scale * (base**e) + offset, min_), max_) for e in range(length)]
