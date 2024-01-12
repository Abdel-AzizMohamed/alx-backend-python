#!/usr/bin/env python3
"""Define sum_mixed_list function"""
from typing import List, Union
import functools


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Gives the sum of a list of floats and integers"""
    return functools.reduce(lambda acc, cur: acc + cur, mxd_lst)
