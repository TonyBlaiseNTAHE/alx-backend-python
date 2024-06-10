#!/usr/bin/env python3
"""Multiple corountines
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    args:
       n: the number of time wait_rondom will be spawn
       max_delay: the time
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    completed_delays = [await task for task in asyncio.as_completed(tasks)]
    return completed_delays
