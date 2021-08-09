import os
from dotenv import load_dotenv


load_dotenv()

ATLAS_USER = os.getenv('ATLAS_USER')
ATLAS_PASS = os.getenv('ATLAS_PASS')
PORT= os.getenv('PORT')

url_mongo = f'mongodb+srv://ATLAS_USER:ATLAS_PASS@cluster0.hxtnv.mongodb.net/'

