from api.police_api import get_crimes
from database.crud import insert_crimes
from export.json_export import export_crimes
from cloud.s3_upload import upload_file


def import_data():
    """
    Download crime data from the Police API and store it in MongoDB.
    """

    print("Downloading crime data...\n")

    crimes = get_crimes()

    print(f"Downloaded {len(crimes):,} crime records.")

    print("\nSaving to MongoDB...")

    inserted = insert_crimes(crimes)

    print(f"Inserted {inserted:,} documents.")


def export_data():
    """
    Export transformed data from MongoDB to JSON.
    """

    print("\nExporting transformed crime data...")

    filename, count = export_crimes()

    print(f"Exported {count:,} records.")

    print(f"JSON saved to: {filename}")

    return filename


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


def main():

    print("=" * 60)
    print("POLICE CRIME ETL PIPELINE")
    print("=" * 60)

    import_data()

    filename = export_data()

    upload_data(filename)

    print("\n" + "=" * 60)
    print("ETL PROCESS COMPLETED SUCCESSFULLY")
    print("=" * 60)



if __name__ == "__main__":
    main()