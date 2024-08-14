#!/usr/bin/env python3

"""
This module provides a function to calculate the sum of elements in a list.

Functions:
- sum_list(input_list: list) -> float: Returns the sum of all elements
  in the input list.

Example:
>>> sum_list([1.5, 2.5, 3.0])
7.0
"""


def sum_list(input_list: list) -> float:
    """
    Calculate the sum of elements in a list.

    Parameters:
    input_list (list): A list of numbers to sum.

    Returns:
    float: The sum of all elements in the input list.

    Example:
    >>> sum_list([1.5, 2.5, 3.0])
    7.0
    """
    return sum(input_list)
