#!/usr/bin/env python3
"""
This module provides asynchronous functionality to run multiple
tasks that wait for random delays, then return the delays in the
order of completion.

Functions:
    task_wait_n(n: int, max_delay: int) -> List[float]:
        Spawns n instances of task_wait_random with the specified
        max_delay and returns a list of delays in the order of
        task completion.
"""

import asyncio
from typing import List

# Import task_wait_random from the module
task_wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns n instances of task_wait_random with a specified max_delay
    and returns a list of delays in the order of task completion.

    Parameters:
        n (int): The number of task_wait_random tasks to spawn.
        max_delay (int): The maximum delay for each task_wait_random task.

    Returns:
        List[float]: A list of delays (float values) in the order of
                     completion of each task.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
