#!/usr/bin/env python3
"""Define task_wait_n function"""
from typing import List
import asyncio


task_wait_random = __import__("3-tasks").task_wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Calls task_wait_random n times with max_delay

    Arguments:
        n: call times of wait_random
        max_delay: time to sleep in wait_random

    Returns:
        List contains slept time in wait_random
    """
    tasks = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )

    return tasks
