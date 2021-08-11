from pymongo import MongoClient

import sys
import os

sys.path.append(os.path.abspath('.'))

from config import url_mongo

client = MongoClient(url_mongo)

def mongo_read(db, coll, q={}, project=None,client=client):
    collection = client.get_database(db)[coll]
    return collection.find(q,project)



