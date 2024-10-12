#!/usr/bin/env python3
"""Type annotation
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """return Tuple
    """
    return (k, v ** 2)
