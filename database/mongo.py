import pymongo
from pymongo import MongoClient

cluster=MongoClient('mongodb+srv://db_bd:IXvSCnEZSNs7LcvZ@cluster0.hxtnv.mongodb.net/db_bdml_21?retryWrites=true&w=majority')
db=cluster['mid_boot_project']
collection=db['matches']

#data uploaded via console with mongoimport