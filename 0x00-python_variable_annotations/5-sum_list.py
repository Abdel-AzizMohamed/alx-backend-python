#!/usr/bin/env python3
"""Define sum_list function"""
import functools


def sum_list(input_list: list[float]) -> float:
    """Gives the sum of a list of floats"""
    return functools.reduce(lambda acc, cur: acc + cur, input_list)
