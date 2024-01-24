#!/usr/bin/env python3
"""
This module creates a Cache class for redis
"""
import redis
import uuid
from typing import Union, Callable
Defr = Union[str, bytes, int, None]


class Cache:
    """
    Class that initialises redis for storing data
    """
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        method to store data to redis using generated
        uuid as key
        Args:
            data: possible data to be cached or made
            redis persistent
        Return:
            Key of the saved data
        """
        key = uuid.uuid4().__str__()
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Defr:
        """
        Method to retrieve data from Redis using a key
        Args:
            key: Key associated with the data
            fn: Optional conversion function to recover the original type
        Return:
            Retrieved data, optionally converted using the provided function
        """
        data = self._redis.get(key)
        if data is not None and fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Union[str, None]:
        """
        Convenience method to retrieve a string from Redis
        Args:
            key: Key associated with the string data
        Return:
            Retrieved string data
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Union[int, None]:
        """
        Convenience method to retrieve an integer from Redis
        Args:
            key: Key associated with the integer data
        Return:
            Retrieved integer data
        """
        return self.get(key, fn=int)
