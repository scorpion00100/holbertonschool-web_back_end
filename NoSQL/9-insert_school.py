#!/usr/bin/env python3
"""9-insert_school module"""


def insert_school(mongo_collection, **kwargs):
    """Insert a new document in a collection"""
    result = mongo_collection.insert_one(kwargs)

    return result.inserted_id
