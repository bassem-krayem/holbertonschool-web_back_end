#!/usr/bin/env python3

"""
This module provides a function to calculate the floor of a float.

Functions:
- floor(n: float) -> int: Returns the largest integer less than or
  equal to the input float.

Example:
>>> floor(7.8)
7
"""

import math


def floor(n: float) -> int:
    """
    Calculate the floor of a float.

    Parameters:
    n (float): The floating-point number to floor.

    Returns:
    int: The largest integer less than or equal to `n`.

    Example:
    >>> floor(7.8)
    7
    """
    return math.floor(n)
