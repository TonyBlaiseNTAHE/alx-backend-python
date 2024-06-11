#!/usr/bin/env python3
"""Async Generator
"""

import asyncio
import random
import time


async def async_generator():
    """function
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(_, 10)
