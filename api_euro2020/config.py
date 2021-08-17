import os

# from dotenv import load_dotenv
# load_dotenv()

#MONGO_URL=os.getenv('MONGO_URL')
#PORT= os.getenv('PORT')
ATLAS_USER = os.getenv("ATLAS_USER")
ATLAS_PASS = os.getenv("ATLAS_PASS")


mongo_url=f'mongodb+srv://{ATLAS_USER}:{ATLAS_PASS}@cluster0.hxtnv.mongodb.net/'

