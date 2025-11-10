#!/usr/bin/env python3

"""
LFU caching system
This module defines a LFUCache class that inherits from BaseCaching
and implements simple put and get methods.
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache class
    Inherits from BaseCaching and implements put and get methods.
    """

    def __init__(self):
        """ Initialize the LFUCache instance. """
        super().__init__()
        self.access_count = {}

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
                min_count = min(self.access_count.values())
                key_to_delete = next(
                    k for k, v in self.access_count.items()
                    if self.access_count[k] == min_count
                )
                del self.access_count[key_to_delete]
                del self.cache_data[key_to_delete]
                print(f"DISCARD: {key_to_delete}")
            if key in self.cache_data:
                self.access_count[key] += 1
                self.cache_data[key] = item
            else:
                self.cache_data[key] = item
                self.access_count[key] = 0

    def get(self, key):
        """
        Retrieves an item from the cache by key.
        Args:
            key (str): The key of the item to retrieve.
        Returns:
            The item associated with the key, or None if the key is not found.
        """
        if key is not None and key in self.cache_data:
            self.access_count[key] += 1
        return self.cache_data.get(key)
