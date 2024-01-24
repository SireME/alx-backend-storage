#!/usr/bin/env python3
"""
This module creates a Cache class for redis
"""
import redis
import uuid
from typing import Union


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
