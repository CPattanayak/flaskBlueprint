from pymongo import MongoClient
import os
mongourl = os.getenv("MONGO-URL","mongodb://localhost:27017")
client = MongoClient(mongourl)
db = client.todoapp
customerCollection=db["order"]