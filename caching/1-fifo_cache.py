#!/usr/bin/env python3

"""
FIFO caching system
This module defines a FIFOCache class that inherits from BaseCaching
and implements simple put and get methods.
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache class
    Inherits from BaseCaching and implements put and get methods.
    """

    def __init__(self):
        """ Initialize the FIFOCache instance. """
        super().__init__()

    def put(self, key, item):
        """
        Adds an item to the cache.
        Args:
            key (str): The key under which the item is stored.
            item (any): The item to store in the cache.
        """
        if key is not None and item is not None:
            if (len(self.cache_data) >= BaseCaching.MAX_ITEMS
                    and key not in self.cache_data):
                key_to_delete = list(self.cache_data.keys())[0]
                del self.cache_data[key_to_delete]
                print(f"DISCARD: {key_to_delete}")
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
