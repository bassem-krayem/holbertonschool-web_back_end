#!/usr/bin/env python3
"""a script that provides some stats about Nginx logs stored in MongoDB:"""

from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017')
col = client.logs.nginx

print(f"{col.count_documents({})} logs")
print("Methods:")
print(f"\tmethod GET: {col.count_documents({'method': 'GET'})}")
print(f"\tmethod POST: {col.count_documents({'method': 'POST'})}")
print(f"\tmethod PUT: {col.count_documents({'method': 'PUT'})}")
print(f"\tmethod PATCH: {col.count_documents({'method': 'PATCH'})}")
print(f"\tmethod DELETE: {col.count_documents({'method': 'DELETE'})}")
print(
    f"{col.count_documents({'method': 'GET', 'path': '/status'})} "
    f"status check"
)
