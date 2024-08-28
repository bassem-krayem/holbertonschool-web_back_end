#!/usr/bin/env python3
"""a Python function that changes all topics of a school document """


def update_topics(mongo_collection, name, topics):
    """a Python function that changes all topics of a school document """
    return mongo_collection.update_many({"name": name},
                                        {"$set": {"topics": topics}})
