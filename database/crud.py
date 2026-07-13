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

def count_crimes():
    """
    Count the number of crime records in MongoDB.

    Returns:
        int: Number of documents in the collection.
    """

    collection = get_collection()

    return collection.count_documents({})

def get_all_crimes():
    """
    Return all crime records from MongoDB.

    Returns:
        list: List of crime documents.
    """

    collection = get_collection()

    return list(collection.find())

def find_by_category(category):
    """
    Return all crime records matching a category.

    Args:
        category (str): Crime category.

    Returns:
        list: List of matching crime documents.
    """
    category = category.strip().lower()
    collection = get_collection()

    return list(
        collection.find(
            {"category": category}
        )
    )

def count_by_category():

    collection = get_collection()
    pipeline = [
        {
            "$group": {
                "_id": "$category",
                "count": {"$sum": 1}
            }
        },
        {
            "$sort": {
                "count": -1
            }
        }
    ]

    return list(collection.aggregate(pipeline))