#!/usr/bin/env python3
"""Type annotations
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """returns a sum of lists of floats
    """
    return float(sum(input_list))
