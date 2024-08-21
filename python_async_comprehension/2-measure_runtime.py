#!/usr/bin/env python3
"""
This module provides functionality to measure the runtime of executing
an asynchronous comprehension multiple times in parallel using
asyncio.gather.

Functions:
    measure_runtime: Measures the total runtime of executing the
    async_comprehension function four times in parallel.
"""

import asyncio
import time

# Import the async_comprehension function from the previous module
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total runtime of executing async_comprehension four
    times in parallel.

    The function uses asyncio.gather to run four instances of the
    async_comprehension function concurrently. The total time taken
    for all four executions is measured and returned.

    Returns:
        float: The total time taken to run the async_comprehension
        function four times in parallel.
    """
    start_time = time.perf_counter()  # Start the time measurement
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.perf_counter()  # End the time measurement

    total_time = end_time - start_time  # Calculate the total runtime
    return total_time  # Return the total runtime
