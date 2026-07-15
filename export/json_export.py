from config import EXPORT_CATEGORIES
import json
from pathlib import Path

from database.crud import get_all_crimes

#uses EXPORT_CATEGORIES from config.py to filter out crime categories that are not in the list. This is used when exporting data to a json file for s3 upload.

def transform_record(crime):
    """
    Transform a MongoDB crime document into an export record.

    Returns:
        dict | None
    """

    return {
        "_id": str(crime["_id"]),
        "category": crime["category"],
        "month": crime["month"],
        "review_status": crime.get("review_status", "Not Reviewed"),

        "street":
            crime["location"]["street"]["name"],

        "latitude":
            crime["location"]["latitude"],

        "longitude":
            crime["location"]["longitude"]
    }



def transform_records(crimes):
    """
    Transform a list of MongoDB crime documents into export records.

    Returns:
        list: List of transformed records.
    """

    transformed = []

    for crime in crimes:

        record = transform_record(crime)

        if record is not None:
            transformed.append(record)

    return transformed



def export_crimes(
    collection_name,
    category=None,
    filename="transformed_crimes.json",
    ):
    """
    Export transformed crime records to a JSON file.

    Args:
        filename (str): Output filename.

    Returns:
        str: Path to exported file.
    """

    crimes = get_all_crimes(collection_name)
    if category is not None:

        crimes = [
            crime
            for crime in crimes
            if crime["category"] == category
        ]

    transformed = transform_records(crimes)

    export_path = Path("exports") / filename
    
    try:
        with open(export_path, "w", encoding="utf-8") as file:

         json.dump(
            transformed,
            file,
            indent=4,
            ensure_ascii=False
        )

    except OSError as err:

        print(f"Export failed: {err}")

        return None, 0

    return str(export_path), len(transformed)