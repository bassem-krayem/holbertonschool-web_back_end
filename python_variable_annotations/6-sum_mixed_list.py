#!/usr/bin/env python3
"""
This module provides a function to calculate the sum of a list containing
both integers and floats.

Functions:
- sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float: Returns the
  sum of all elements in the list, which can contain both integers and
  floats.

Example:
>>> sum_mixed_list([1, 2.5, 3, 4.5])
11.0
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a list containing both integers and floats.

    Parameters:
    mxd_lst (List[Union[int, float]]): A list of integers and/or floats.

    Returns:
    float: The sum of all elements in the list, cast to float.

    Example:
    >>> sum_mixed_list([1, 2.5, 3, 4.5])
    11.0
    """
    return sum(mxd_lst)
