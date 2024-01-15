#!/usr/bin/env python3
"""Define wait_random function"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait form 0 to max_delay Asynchronously"""
    delay = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
