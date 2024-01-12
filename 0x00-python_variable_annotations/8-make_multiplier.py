#!/usr/bin/env python3
"""Define to_kv function"""
from typing import Callable


def multiple(num: float) -> float:
    """Gives the power 2 of a number"""
    return num * num


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Gives the sum of a list of floats and integers"""
    return multiple


print(make_multiplier.__annotations__)
fun = make_multiplier(2.22)
print("{}".format(fun(2.22)))
