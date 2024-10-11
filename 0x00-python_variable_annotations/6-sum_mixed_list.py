#!/usr/bin/env python3
"""Type annotation
"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """A function that returns their sum as a float
    mxd_lst: list of integers and floats
    """
    return float(sum(mxd_lst))
