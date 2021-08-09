from utils.json_response import json_response
from app import app
from flask import request
from utils.handle_error import handle_error

@app.route("/")
@handle_error
def example_fn():
    student = {
        'project':'Euro2020',
        'grade':'A+'
    }
    return json_response(student)

@app.route("/hello")
@handle_error
def hello_fn():     
    print('terminal test')
    print(request.args)
    name = request.args.get("name",'no name')
    surname = request.args.get('surname', 'no surname')
    #raise ValueError('MEC')
    return {
        'name': "test "+name,
        'surname': surname
    }
        


 