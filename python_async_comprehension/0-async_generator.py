#!/usr/bin/env python3
"""
This module demonstrates the use of an asynchronous generator
that yields random float numbers between 0 and 10. The generator
produces one number every second, for a total of 10 numbers.

Functions:
    async_generator: An asynchronous generator function that yields
    a random float between 0 and 10 every second.
"""

import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    An asynchronous generator that yields a random float
    between 0 and 10 every second. This function generates
    a total of 10 random numbers.

    Yields:
        float: A random float between 0 and 10.
    """
    for i in range(10):
        await asyncio.sleep(1)  # Pause for 1 second
        random_number = random.uniform(0, 10)  # Generate a random float
        yield random_number  # Yield the random number
