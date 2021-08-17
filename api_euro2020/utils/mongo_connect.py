from utils.json_response import str_json
from pymongo import MongoClient

import sys
import os
from config import mongo_url

sys.path.append(os.path.abspath('.'))

client = MongoClient(mongo_url)

def mongo_read(db, coll, query={}, project={'_id':0},client=client):
    collection = client.get_database(db)[coll]
    return collection.find(query,project)



