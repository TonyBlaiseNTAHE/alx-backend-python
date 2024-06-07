#!/usr/bin/env python3
"""Type of annotation
"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[float, int]]) -> float:
    """
    args:
     input_list:  a list of floats and integers
    returns: the sum of floats
    """
    sum = 0
    for i in range(len(mxd_list)):
        sum += mxd_list[i]
    return sum
