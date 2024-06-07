#!/usr/bin/env python3
"""Type annotaion function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    args:
      multiplier: float
    returns:  a function that multipliers floats

    """
    def func(x: float) -> float:
        """
        args: x: a float
        return: the multiplication of two floats
        """
        return x * multiplier
    return func
