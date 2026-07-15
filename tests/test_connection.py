from database.mongo import get_collection

collection = get_collection()

print(collection.name)