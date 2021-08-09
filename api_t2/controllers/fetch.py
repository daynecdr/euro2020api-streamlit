from app import app
from flask import request
from utils.json_response import json_response
from utils.mongo_connect import mongo_read

@app.get('/')
def read_mongo():
    q = dict(request.args)
    print (q)
   
    return {json_response(list(mongo_read('mid_boot_project','player_stats')))}