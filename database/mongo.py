# database/mongo.py

import os

from dotenv import load_dotenv
from pymongo import MongoClient


load_dotenv()


def get_collection():
    """
    Connect to MongoDB and return the collection.
    """

    mongo_uri = os.getenv("MONGO_URI")
    database_name = os.getenv("DATABASE_NAME")
    collection_name = os.getenv("COLLECTION_NAME")

    client = MongoClient(mongo_uri)

    db = client[database_name]

    collection = db[collection_name]

    return collection