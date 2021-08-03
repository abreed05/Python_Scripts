import pymongo
import os
import hvac
import urllib.parse
import config

try:
    client = config.mongo_connect()
    mongo_db = client["hcv"]
    mongo_collection = mongo_db["tests"]
    mongo_dict = {"name": "Test", "version": 2}
    print("I made it here")
    x = mongo_collection.insert_one(mongo_dict)

except Exception:
    print("Unable to insert document into collection")