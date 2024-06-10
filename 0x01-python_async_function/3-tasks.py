#!/usr/bin/env python3
"""Computing tasks
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> int:
    """
    args:
      max_delay: the time
    """
    task = wait_random(max_delay)
    return asyncio.Task(task)
