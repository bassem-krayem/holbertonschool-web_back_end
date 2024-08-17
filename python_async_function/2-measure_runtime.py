#!/usr/bin/env python3
"""
This module provides a utility function to measure the average execution
time of running multiple asynchronous tasks using the `wait_n` function.
The average execution time is calculated by measuring the total elapsed
time for all tasks and then dividing by the number of tasks.

Functions:
    measure_time(n: int, max_delay: int) -> float:
        Measures and returns the average execution time for `n` 
        asynchronous tasks with a specified maximum delay.
"""

import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the average execution time for running `n` asynchronous
    tasks using the `wait_n` function with a specified maximum delay.

    Args:
        n (int): The number of asynchronous tasks to run concurrently.
        max_delay (int): The maximum delay (in seconds) for each task.

    Returns:
        float: The average execution time per task. This is calculated
               as the total time taken divided by the number of tasks.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    
    total_execution_time = end_time - start_time
    return total_execution_time / n
