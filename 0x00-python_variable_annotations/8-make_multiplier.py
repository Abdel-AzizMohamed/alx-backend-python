#!/usr/bin/env python3
"""Define to_kv function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Gives the sum of a list of floats and integers"""
    return lambda x: x * multiplier
