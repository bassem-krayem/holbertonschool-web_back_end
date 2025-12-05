#!/usr/bin/env python3
''' Redis Module '''
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    ''' def count calls '''
    @wraps(method)
    def wrapper(self, *args, **kwds):
        ''' def wrapper '''
        key_m = method.__qualname__
        self._redis.incr(key_m)
        return method(self, *args, **kwds)
    return wrapper


def call_history(method: Callable) -> Callable:
    ''' def call history '''
    @wraps(method)
    def wrapper(self, *args, **kwds):
        ''' def wrapper'''
        key_m = method.__qualname__
        inp_m = key_m + ':inputs'
        outp_m = key_m + ":outputs"
        data = str(args)
        self._redis.rpush(inp_m, data)
        fin = method(self, *args, **kwds)
        self._redis.rpush(outp_m, str(fin))
        return fin
    return wrapper


def replay(method: Callable):
    """Display the history of calls of a particular function."""
    # Try to get the redis instance from the bound method (method.__self__),
    # otherwise fall back to a new client.
    redis_client = None
    if hasattr(method, "__self__") and method.__self__ is not None:
        # bound method: use the instance redis
        redis_client = method.__self__._redis
    else:
        # fallback (unbound function) -- use default redis connection
        redis_client = redis.Redis()

    key = method.__qualname__
    inputs = redis_client.lrange(f"{key}:inputs", 0, -1)
    outputs = redis_client.lrange(f"{key}:outputs", 0, -1)

    calls_number = len(inputs)
    times_str = "time" if calls_number == 1 else "times"
    print(f"{key} was called {calls_number} {times_str}:")

    for inp, out in zip(inputs, outputs):
        # decode bytes to string; keep the original tuple-format representation
        inp_str = inp.decode("utf-8")
        out_str = out.decode("utf-8")
        print(f"{key}(*{inp_str}) -> {out_str}")


class Cache():
    ''' class cache '''
    def __init__(self):
        ''' def init '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        ''' def store '''
        gen = str(uuid.uuid4())
        self._redis.set(gen, data)
        return gen

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        ''' def get '''
        value = self._redis.get(key)
        return value if not fn else fn(value)

    def get_int(self, key):
        return self.get(key, int)

    def get_str(self, key):
        value = self._redis.get(key)
        return value.decode("utf-8")
