from utils.json_response import json_response
from app import app
from flask import request
from utils.handle_error import handle_error

@app.route("/two")
@handle_error
def two_():    
    return {'some data':'good grades'}


 