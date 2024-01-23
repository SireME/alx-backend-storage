#!/usr/bin/env python3
"""
This modules contains a Python function that
 inserts a new document in a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
    insert new document in a collection
    Args:
         mongo_collection: pymongo clollection object
         kwargs: objects(dictionaries to insert)
    Return:
          id of the object inserted
    """
    inserted = mongo_collection.insert_one(kwargs)
    return inserted.inserted_id
