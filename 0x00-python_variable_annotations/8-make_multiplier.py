#!/usr/bin/env python3
"""Type annotation
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """type annotation
    """
    def fun(y: float) -> float:
        return y * multiplier
    return fun
