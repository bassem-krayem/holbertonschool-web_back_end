#!/usr/bin/env python3

"""
This module provides a function to create a multiplier function.

Functions:
- make_multiplier(multiplier: float) -> Callable[[float], float]: Returns
  a function that multiplies its input by the specified multiplier.

Example:
>>> double = make_multiplier(2.0)
>>> double(5.0)
10.0
>>> triple = make_multiplier(3.0)
>>> triple(5.0)
15.0
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a multiplier function that multiplies its input by the given
    multiplier.

    Parameters:
    multiplier (float): The factor by which the input will be multiplied.

    Returns:
    Callable[[float], float]: A function that takes a float as input and
    returns a float, representing the input multiplied by the multiplier.

    Example:
    >>> double = make_multiplier(2.0)
    >>> double(5.0)
    10.0
    >>> triple = make_multiplier(3.0)
    >>> triple(5.0)
    15.0
    """
    def mul(x: float) -> float:
        """
        Multiply the input by the multiplier.

        Parameters:
        x (float): The value to be multiplied.

        Returns:
        float: The result of multiplying `x` by `multiplier`.

        Example:
        >>> mul(5.0)
        10.0
        """
        return x * multiplier

    return mul
