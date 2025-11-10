#!/usr/bin/env python3

"""
BasicCache module
Defines a BasicCache class that inherits from BaseCaching
and implements simple put and get methods.
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache class
    Inherits from BaseCaching and implements put and get methods.
    """

    def put(self, key, item):
        """
        Adds an item to the cache.
        Args:
            key (str): The key under which the item is stored.
            item (any): The item to store in the cache.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves an item from the cache by key.
        Args:
            key (str): The key of the item to retrieve.
        Returns:
            The item associated with the key, or None if the key is not found.
        """
        return self.cache_data.get(key)
