from utils.json_response import str_json
from pymongo import MongoClient

import sys
import os
from config import MONGO_URL

sys.path.append(os.path.abspath('.'))

client = MongoClient(MONGO_URL)

def mongo_read(db, coll, query={}, project={'_id':0},client=client):
    collection = client.get_database(db)[coll]
    return collection.find(query,project)



