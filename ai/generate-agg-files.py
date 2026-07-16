from pymongo import MongoClient
import os
from dotenv import load_dotenv
import datetime

# set file path
path = os.path.dirname(os.path.realpath(__file__))

# download data from mongodb
# get mongo setting from env
mongo_uri = os.getenv("MONGO_URI")
database_name = os.getenv("DATABASE_NAME")

# set mongo db
client = MongoClient(mongo_uri)
db = client[database_name]

# list available data
collections = db.list_collection_names()

# loop through collections and create aggregate strings for each
for col in collections:
    col_info = col.split("_")
    # get city name from collection
    city = col_info[0]
    # format month as text and add year
    period = datetime.date(int(col_info[1]), int(col_info[2]), 1).strftime('%B')
    period+= " " + col_info[1]

    # set up file to write outputs to
    f = open(f"{path}/data/{col}.txt", "x")

    # add total crime in city to list
    total = db[col].count_documents({})
    str_total = f"{city} had {total} total crimes in {period}\n"
    # add to list
    f.write(str_total)

    # crimes per category
    categories = db[col].distinct("category")
    cat_counts = {}
    for cat in categories:
        cat_total = db[col].count_documents({"category":cat})
        cat_counts.update({cat:cat_total})
        if cat_total == 1:
            str_cat_tot = f"There was {cat_total} incident of {cat} in {city} in {period}\n"
        else:
            str_cat_tot = f"There were {cat_total} incidents of {cat} in {city} in {period}\n"
        f.write(str_cat_tot)

    # most common crime type
    str_max = f"{max(cat_counts, key=cat_counts.get)} was the most common in {city} in {period}"
    f.write(str_max)

    # close text file
    f.close()