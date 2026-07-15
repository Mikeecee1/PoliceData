

from api.police_api import get_crimes
from database.crud import count_by_category, insert_crimes
from export.json_export import export_crimes
from cloud.s3_upload import upload_file
from ui.menu import choose_collection_name, choose_export_category, choose_location, choose_month, confirm_upload


################################
#     HELPER FUNCTIONS         #
################################ 

def import_data(
    latitude,
    longitude,
    month,
    collection_name,
):
    """
    Download crime data from the Police API and store it in MongoDB.
    """

    print("Downloading crime data...\n")

    crimes = get_crimes(
    latitude=latitude,
    longitude=longitude,
    month=month,
)

    print(f"Downloaded {len(crimes):,} crime records.")

    print("\nSaving to MongoDB...")

    inserted = insert_crimes(crimes, collection_name)

    print(f"Inserted {inserted:,} documents.")

#Unused function, but could be useful for future development
# def export_data():
#     """
#     Export transformed data from MongoDB to JSON.
#     """

#     print("\nExporting transformed crime data...")

#     filename, count = export_crimes()

#     print(f"Exported {count:,} records.")

#     print(f"JSON saved to: {filename}")

#     return filename


def upload_data(filename):
    """
    Upload a JSON export to S3.
    """

    print("\nUploading to AWS S3...")

    success = upload_file(filename)

    if success:
        print("Upload completed successfully.")
    else:
        print("Upload failed.")


def build_export_filename(collection_name, crime_type):
    """
    Create a consistent JSON export filename.
    """
    crime = crime_type.replace("-", "_")

    return f"{collection_name}_{crime}.json"
##Unused function, but could be useful for future development##
# def show_crime_summary(collection_name):
#     """
#     Display the five most common crime categories.
#     """

#     print("\n" + "=" * 60)
#     print("TOP 5 CRIME CATEGORIES")
#     print("=" * 60)

#     counts = count_by_category(collection_name)

#     for row in counts[:5]:

#         crime = row["_id"].replace("-", " ").title()

#         print(f"{crime:<30}{row['count']:>6}")

#     return counts

def main():

    print("=" * 60)
    print("POLICE CRIME ETL PIPELINE")
    print("=" * 60)

    location = choose_location()

    print(f"Selected location: {location['name']}")

    month = choose_month()

    print(f"Selected month: {month}")

    default_collection = (
    f"{location['name']}_{month.replace('-', '_')}"
    )

    collection_name = choose_collection_name(default_collection)

    print("\n" + "=" * 60)
    print("CURRENT SELECTION")
    print("=" * 60)

    print(f"Location        : {location['name']}")
    print(f"Month           : {month}")
    print(f"Collection Name : {collection_name}")

    import_data(location["latitude"], location["longitude"], month, collection_name)
    counts = count_by_category(collection_name)

    selected_category = choose_export_category(counts)

    filename = build_export_filename(
        collection_name,
        selected_category or "all",
    )

    filename, count = export_crimes(
        collection_name,
        selected_category,
        filename,
    )

    print("\n" + "=" * 60)
    print("ETL PROCESS COMPLETED SUCCESSFULLY")
    print("=" * 60)
    print("\n" + "=" * 60)
    

    if confirm_upload():

        upload_data(filename)
        print("EXPORT COMPLETE")
        print("=" * 60)

        print(f"Records exported : {count:,}")
        print(f"Export file      : {filename}")

    else:

        print("\nUPLOAD CANCELLED.")
        print("=" * 60)

    



if __name__ == "__main__":
    main()