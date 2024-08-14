#!/usr/bin/env python3
"""
This module provides a function to create a tuple from a key and the square
of a value.

Functions:
- to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]: Returns a
  tuple containing the key and the square of the value.

Example:
>>> to_kv('age', 5)
('age', 25.0)
>>> to_kv('height', 2.5)
('height', 6.25)
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple containing a key and the square of a value.

    Parameters:
    k (str): The key to include in the tuple.
    v (Union[int, float]): The value to be squared and included in the tuple.

    Returns:
    Tuple[str, float]: A tuple where the first element is the key `k`, and
    the second element is the square of the value `v`.

    Example:
    >>> to_kv('age', 5)
    ('age', 25.0)
    >>> to_kv('height', 2.5)
    ('height', 6.25)
    """
    return (k, v * v)
