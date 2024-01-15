#!/usr/bin/env python3
"""Define measure_time function"""
import time
import asyncio


wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Calls wait_n and measures the total execution time

    Arguments:
        n: call times of wait_random
        max_delay: time to sleep in wait_random

    Returns:
        total execution time
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))

    return (time.time() - start_time) / n
