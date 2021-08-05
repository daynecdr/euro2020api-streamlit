from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return 'hello'
# @app.route("/")    
# def index():
#     return json.dumps({'this':'is a test'})


