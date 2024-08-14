#!/usr/bin/env python3
"""
This module provides a function to repeat each element of a tuple a specified
number of times and return the result as a list.

Functions:
- zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
  Repeats each element in the tuple `lst` `factor` times and returns the
  result as a list.

Example:
>>> zoom_array((12, 72, 91))
[12, 12, 72, 72, 91, 91]

>>> zoom_array((12, 72, 91), 3)
[12, 12, 12, 72, 72, 72, 91, 91, 91]
"""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Repeat each element of a tuple `factor` times.

    Parameters:
    lst (Tuple[int, ...]): A tuple of integers to be repeated.
    factor (int): The number of times each element should be repeated.
                  Defaults to 2.

    Returns:
    List[int]: A list with each element from the input tuple repeated
               `factor` times.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


# Correctly typed as Tuple[int, ...] to match the function input type
array: Tuple[int, int, int] = (12, 72, 91)

zoom_2x: List[int] = zoom_array(array)

# Using an integer for `factor`, and `array` is already a Tuple
zoom_3x: List[int] = zoom_array(array, 3)
