from utils.json_response import str_json
from pymongo import MongoClient

import sys
import os

sys.path.append(os.path.abspath('.'))

from config import MONGO_URL

client = MongoClient(MONGO_URL)

def mongo_read(db, coll, query={}, project={'_id':0},client=client):
    # for k,v in query.items():
    #     if '{' in v:
    #         query[k] = str_json

    collection = client.get_database(db)[coll]
    return collection.find(query,project)



