#!/usr/bin/env python3
"""Type of annotation
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    args:
     input_list:  a list of floats
    returns: the sum of floats
    """
    sum = 0
    for i in range(len(input_list)):
        sum += input_list[i]
    return sum
