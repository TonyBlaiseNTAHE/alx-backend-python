#!/usr/bin/env python3
"""Multiple corountines
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    args:
       n: the number of time wait_rondom will be spawn
       max_delay: the time
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    return await asyncio.gather(*tasks)
