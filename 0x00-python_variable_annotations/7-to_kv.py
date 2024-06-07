#!/usr/bin/env python3
"""Type annotaion function
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    args: k: str
        v: int or float
    returns a tuple
    """
    return (k, v ** 2)
