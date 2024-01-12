#!/usr/bin/env python3
"""Define sum_list function"""
from typing import List
import functools


def sum_list(input_list: List[float]) -> float:
    """Gives the sum of a list of floats"""
    return functools.reduce(lambda acc, cur: acc + cur, input_list)
