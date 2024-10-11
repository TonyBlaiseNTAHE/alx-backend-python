#!/usr/bin/env python3
"""Type annotation
"""
from typing import Union


def sum_mixed_list(mxd_lst: Union[int, float]) -> float:
    """A function that returns their sum as a float
    mxd_lst: list of integers and floats
    """
    return sum(mxd_lst)
