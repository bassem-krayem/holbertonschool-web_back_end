#!/usr/bin/env python3
"""This module defines a Cache class that interacts with a Redis database to
store data."""
import redis
from uuid import uuid4


class Cache:
    """Cache class for storing data in Redis."""
    def __init__(self) -> None:
        """Initialize the Cache with a Redis client and flush the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: str | bytes | int | float) -> str:
        """Store the input data in Redis and return the generated key."""
        key = str(uuid4())
        self._redis.set(key, data)
        return key
