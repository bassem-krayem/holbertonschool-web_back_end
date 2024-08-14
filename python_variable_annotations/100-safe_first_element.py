#!/usr/bin/env python3
"""
This module provides a function to safely get the first element of a
sequence.

Functions:
- safe_first_element(lst: Sequence[Any]) -> Optional[Any]: Returns the
  first element of the sequence if it exists; otherwise, returns None.

Example:
>>> safe_first_element([1, 2, 3])
1
>>> safe_first_element([])
None
>>> safe_first_element(('a', 'b', 'c'))
'a'
"""

from typing import Optional, Any, Sequence


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    Safely get the first element of a sequence.

    Parameters:
    lst (Sequence[Any]): A sequence (e.g., list, tuple, or string).

    Returns:
    Optional[Any]: The first element of the sequence if it exists; otherwise,
    None.

    Example:
    >>> safe_first_element([1, 2, 3])
    1
    >>> safe_first_element([])
    None
    >>> safe_first_element(('a', 'b', 'c'))
    'a'
    """
    if lst:
        return lst[0]
    else:
        return None
