from app import app
#from config import PORT
from controllers.fetch import *
import os

app.run("0.0.0.0",os.getenv("PORT"),debug=True)