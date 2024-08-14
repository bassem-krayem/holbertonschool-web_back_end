#!/usr/bin/env python3

"""
This module provides a function to safely retrieve a value from a
dictionary with a default fallback.

Functions:
- safely_get_value(dct: Mapping[Any, Any],
                   key: Any,
                   default: Union[T, None] = None) -> Union[Any, T]:
  Retrieves the value associated with the given key from the dictionary.
  If the key is not found, it returns the default value.

  Parameters:
  dct (Mapping[Any, Any]): A dictionary to search for the key.
  key (Any): The key to look up in the dictionary.
  default (Union[T, None]): The value to return if the key is not found.
                             Defaults to None. Can be of any type.

  Returns:
  Union[Any, T]: The value associated with the key if found; otherwise,
  the default value. The default value can be of any type.
"""

from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, Any],
                     key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely get a value from a dictionary with a default fallback.

    Parameters:
    dct (Mapping[Any, Any]): A dictionary from which to get the value.
    key (Any): The key to look up in the dictionary.
    default (Union[T, None]): The value to return if the key is not found.
                              Defaults to None. Can be of any type.

    Returns:
    Union[Any, T]: The value associated with the key if found; otherwise,
    the default value. The default value can be of any type.
"""
    if key in dct:
        return dct[key]
    else:
        return default
