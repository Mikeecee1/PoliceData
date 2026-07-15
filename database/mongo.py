# database/mongo.py

import os

from dotenv import load_dotenv
from pymongo import MongoClient


load_dotenv()

def get_collection(collection_name=None):
    """
    Connect to MongoDB and return the requested collection.

    Args:
        collection_name (str, optional): Collection to use.
            If omitted, uses COLLECTION_NAME from .env.
    """

    mongo_uri = os.getenv("MONGO_URI")
    database_name = os.getenv("DATABASE_NAME")

    if collection_name is None:
        collection_name = os.getenv("COLLECTION_NAME")

    client = MongoClient(mongo_uri)

    db = client[database_name]

    return db[collection_name]