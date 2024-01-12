#!/usr/bin/env python3
"""Define to_kv function"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Gives a list contains tuples"""
    return [(i, len(i)) for i in lst]
