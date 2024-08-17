#!/usr/bin/env python3
"""
This module provides a function to measure the average execution time
of running multiple asynchronous tasks using the `wait_n` function.
"""

import time  # Import the time module to measure execution time
import asyncio  # Import asyncio for running asynchronous functions

# Import the wait_n function from the 1-concurrent_coroutines module
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for running the wait_n function
    with `n` asynchronous tasks and a maximum delay of `max_delay`.

    Args:
        n (int): Number of asynchronous tasks to run.
        max_delay (int): Maximum delay for each task.

    Returns:
        float: The average execution time per task.
    """
    start_time = time.time()  # Record the start time before execution
    asyncio.run(wait_n(n, max_delay))  # Run the wait_n function
    end_time = time.time()  # Record the end time after execution
    
    # Calculate total execution time and return average time per task
    execution_time = end_time - start_time
    return execution_time / n
