#!/usr/bin/env python3
"""
This module provides a function to create and return an asyncio.Task
object for the `wait_random` function imported from `0-basic_async_syntax`.

Functions:
    task_wait_random(max_delay: int) -> asyncio.Task:
        Creates and returns an asyncio.Task object for the `wait_random`
        function with a specified maximum delay.
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio.Task for the wait_random function with a given
    maximum delay.

    Args:
        max_delay (int): The maximum delay (in seconds) for the wait_random
                         function.

    Returns:
        asyncio.Task: An asyncio.Task object that represents the asynchronous
                       execution of the wait_random function.
    """
    return asyncio.create_task(wait_random(max_delay))
