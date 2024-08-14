#!/usr/bin/env python3
"""
This module provides a function to calculate the length of each element in
an iterable of sequences.

Functions:
- element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
  Returns a list of tuples where each tuple contains a sequence from the
  input iterable and its length.

Example:
>>> element_length(['hello', 'world', 'python'])
[('hello', 5), ('world', 5), ('python', 6)]
>>> element_length([[1, 2], [1, 2, 3], [1]])
[([1, 2], 2), ([1, 2, 3], 3), ([1], 1)]
"""

from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of each element in an iterable of sequences.

    Parameters:
    lst (Iterable[Sequence]): An iterable where each element is a sequence
    (e.g., list, string, tuple).

    Returns:
    List[Tuple[Sequence, int]]: A list of tuples where each tuple contains
    a sequence from the input iterable and its length.

    Example:
    >>> element_length(['hello', 'world', 'python'])
    [('hello', 5), ('world', 5), ('python', 6)]
    >>> element_length([[1, 2], [1, 2, 3], [1]])
    [([1, 2], 2), ([1, 2, 3], 3), ([1], 1)]
    """
    return [(i, len(i)) for i in lst]
