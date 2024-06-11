#!/usr/bin/env python3
"""parallel comprehensions
"""


import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """
    """
    start_time = time.perf_counter()
    await asyncio.gather(async_comprehension())
    total_time = time.perf_counter() - start_time
    return total_time
