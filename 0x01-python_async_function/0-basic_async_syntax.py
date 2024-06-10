#!/usr/bin/env python3
"""basic of async
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    args:
      max_delay: the number of second the function have to wait
    returns: a float
    """
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
