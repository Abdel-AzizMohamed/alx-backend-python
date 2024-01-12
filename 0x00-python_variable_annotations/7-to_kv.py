#!/usr/bin/env python3
"""Define to_kv function"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Gives the sum of a list of floats and integers"""
    return (k, v * v)
