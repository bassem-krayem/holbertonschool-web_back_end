#!/usr/bin/env python3

"""
This module provides a function to concatenate two strings.

Functions:
- concat(str1: str, str2: str) -> str: Returns the concatenation of
  two strings.

Example:
>>> concat("Hello, ", "world!")
'Hello, world!'
"""


def concat(str1: str, str2: str) -> str:
    """
    Concatenate two strings.

    Parameters:
    str1 (str): The first string to concatenate.
    str2 (str): The second string to concatenate.

    Returns:
    str: The concatenated result of `str1` and `str2`.

    Example:
    >>> concat("Hello, ", "world!")
    'Hello, world!'
    """
    return str1 + str2
