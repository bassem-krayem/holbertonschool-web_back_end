#!/usr/bin/env python3
"""a Python function that inserts a new document in a collection """


def insert_school(mongo_collection, **kwargs):
    """a Python function that inserts a new document in a collection """
    return mongo_collection.insert_one(kwargs).inserted_id


if __name__ == "__main__":
    insert_school(mongo_collection)
