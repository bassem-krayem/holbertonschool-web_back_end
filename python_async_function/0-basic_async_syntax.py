#!/usr/bin/env python3
"""
This module provides an asynchronous function, wait_random,
that introduces a random delay before returning the delay
time.

Functions:
    wait_random(max_delay: int = 10) -> float:
        Waits for a random delay between 0 and max_delay
        (inclusive) seconds and returns the delay time.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay seconds.

    Parameters:
        max_delay (int): The maximum delay in seconds. Default
                         is 10 seconds.

    Returns:
        float: The actual delay time in seconds.
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
