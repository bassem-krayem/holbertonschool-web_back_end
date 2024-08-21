#!/usr/bin/env python3
"""
This module provides a function for collecting numbers from an
asynchronous generator using asyncio and asynchronous comprehensions.

Functions:
    async_comprehension: Collects numbers from the async_generator
    and returns them as a list.
"""

import _asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects numbers from the async_generator using an async
    comprehension and returns them as a list.

    The function utilizes an asynchronous generator to yield
    numbers, and an asynchronous comprehension is used to
    collect these numbers into a list.

    Returns:
        List: A list of numbers collected from the async_generator.
    """
    numbers = [number async for number in async_generator()]
    return numbers
