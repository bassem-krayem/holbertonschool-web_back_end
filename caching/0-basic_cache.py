#!/usr/bin/env python3
"""
BasicCache module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache defines a simple caching system with no limit."""

    def put(self, key, item):
        """Add an item in the cache.

        If either key or item is None, do nothing.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Return the value linked to key.

        If key is None or doesn’t exist, return None.
        """
        if key is None:
            return None
        return self.cache_data.get(key)
