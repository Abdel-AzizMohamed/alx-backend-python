#!/usr/bin/env python3
"""Define wait_random function"""
from typing import List
import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[int]:
    """
    Calls wait_random n times with max_delay

    Arguments:
        n: call times of wait_random
        max_delay: time to sleep in wait_random

    Returns:
        List contains slept time in wait_random
    """
    sleep_time = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )

    return sleep_time
