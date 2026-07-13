# database/crud.py

from database.mongo import get_collection


def insert_crimes(crimes):
    """
    Insert a list of crime records into MongoDB.

    Args:
        crimes (list): List of dictionaries from the Police API.

    Returns:
        int: Number of documents inserted.
    """

    collection = get_collection()

    result = collection.insert_many(crimes)

    return len(result.inserted_ids)

