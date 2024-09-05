#!/usr/bin/env python3

def top_students(mongo_collection):
    return mongo_collection.find().sort({"averageScore": -1})
