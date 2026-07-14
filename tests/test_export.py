from export.json_export import export_crimes


def main():

    print("=" * 60)
    print("JSON EXPORT TEST")
    print("=" * 60)

    filename, count = export_crimes()

    print(f"\nExport completed successfully.")
    print(f"Records exported : {count:,}")
    print(f"Output file      : {filename}")


if __name__ == "__main__":
    main()