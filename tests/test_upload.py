from cloud.s3_upload import upload_file


def main():

    print("=" * 60)
    print("S3 UPLOAD TEST")
    print("=" * 60)

    success = upload_file("exports/transformed_crimes.json")

    if success:
        print("\nUpload completed successfully.")
    else:
        print("\nUpload failed.")


if __name__ == "__main__":
    main()