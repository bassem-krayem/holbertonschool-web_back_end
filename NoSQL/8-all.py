#!/usr/bin/env python3
"""a Python function that lists all documents in a collection"""


def list_all(mongo_collection):
    """a Python function that lists all documents in a collection"""
    return mongo_collection.find()


if __name__ == "__main__":
    list_all(mongo_collection)
