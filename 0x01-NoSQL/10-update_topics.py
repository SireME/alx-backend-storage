#!/usr/bin/env python3
"""
This modules contains a Python function that
 changes all topics of a school document based on the name
"""


def update_topics(mongo_collection, name, topics):
    """
    changes all topics of a school document
    based on name
    aArgs:
          mongo_collection:
          name:
          topics:
    Return:
           None
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
