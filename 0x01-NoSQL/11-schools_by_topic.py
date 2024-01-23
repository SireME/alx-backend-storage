#!/usr/bin/env python3
"""
This modules contains a Python function that
 returns the list of school having a specific topic:
"""

def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of schools that have a specific topic.
    
    Args:
        mongo_collection: pymongo collection object
        topic (str): Topic to search for
    
    Returns:
        list: List of schools matching the specified topic
    """
    result = mongo_collection.find({"topics": topic})

    return list(result)
