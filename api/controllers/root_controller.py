from utils.json_response import json_response
from app import app

@app.route("/")
def example():
    student = {
        'name':'Gonz',
        'grade':'A+'
    }
    return json_response(student)