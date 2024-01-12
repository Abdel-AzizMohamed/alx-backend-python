#!/usr/bin/env python3
"""Define to_kv function"""
from typing import Mapping, Union, Any, TypeVar

T = TypeVar("T")


def safely_get_value(
    dct: Mapping, key: str, default: None = Union[Any, T]
) -> Union[Any, T]:
    """Return the given key if its exists else return the default value"""
    if key in dct:
        return dct[key]
    else:
        return default
