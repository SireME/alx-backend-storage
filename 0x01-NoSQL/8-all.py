#!/usr/bin/env python3
"""
This modules contains a Python function that
lists all documents in a collection
"""


def list_all(mongo_collection):
    """
    list all documents in a collection
    Args:
         mongo_collection: mongo clollection object
    Return:
           empty list or list of collection objects
    """
    return [i for i in mongo_collection.find()]
