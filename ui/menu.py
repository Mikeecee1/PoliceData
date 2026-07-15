from config import LOCATIONS, AVAILABLE_MONTHS


def choose_location():

    print("\nAvailable Locations\n")

    for key, location in LOCATIONS.items():

        print(f"{key}. {location['name']}")

    while True:

        choice = input("\nSelect location: ").strip()

        if choice in LOCATIONS:
            return LOCATIONS[choice]

        print("Invalid selection.")


def choose_month():

    print("\nAvailable Months\n")

    months = AVAILABLE_MONTHS

    for i, month in enumerate(months, start=1):

        print(f"{i}. {month}")

    while True:

        choice = input("\nSelect month: ").strip()

        if choice.isdigit() and 1 <= int(choice) <= len(months):

            return months[int(choice) - 1]

        print("Invalid selection.")


def choose_collection_name(default_name):
    """
    Prompt the user for a MongoDB collection name.

    Pressing Enter accepts the suggested default.
    """

    print("\nCollection Name")

    name = input(
        f"Press Enter for '{default_name}' or type a new name: "
    ).strip()

    if not name:
        return default_name

    return name

def choose_export_category(counts):
    """
    Display the top five crime categories and allow the user to
    choose one for export.

    Returns:
        str | None: Selected category, or None for all categories.
    """

    top_categories = counts[:5]

    print("\n" + "=" * 60)
    print("SELECT CRIME CATEGORY TO EXPORT")
    print("=" * 60)

    for i, row in enumerate(top_categories, start=1):

        crime = row["_id"].replace("-", " ").title()

        print(f"{i}. {crime:<30}{row['count']:>6}")

    print(f"{len(top_categories) + 1}. All Categories")

    while True:

        choice = input("\nSelect option: ").strip()

        if choice.isdigit():

            choice = int(choice)

            if 1 <= choice <= len(top_categories):
                return top_categories[choice - 1]["_id"]

            if choice == len(top_categories) + 1:
                return None

        print("Invalid selection.")

def confirm_upload():
    """
    Ask the user whether to upload the exported file.
    """

    while True:

        choice = input(
            "\nUpload file to AWS S3? (Y/N): "
        ).strip().upper()

        if choice in ("Y", "N"):
            return choice == "Y"

        print("Please enter Y or N.")