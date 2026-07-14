from database.crud import (
    add_crime,
    count_crimes,
    get_all_crimes,
    find_by_category,
    count_by_category,
    update_crime_status,
    delete_crime,
)


def main():

    print("=" * 60)
    print("MONGODB CRUD FUNCTION TESTS")
    print("=" * 60)

    # -------------------------------------------------------
    # Count Crimes
    # -------------------------------------------------------

    total = count_crimes()

    print(f"\nTotal crime records: {total:,}")

    # -------------------------------------------------------
    # Get All Crimes
    # -------------------------------------------------------

    crimes = get_all_crimes()

    print(f"\nRetrieved {len(crimes):,} documents.")

    print("\nFirst document:\n")

    print(crimes[0])

    # -------------------------------------------------------
    # Find by Category
    # -------------------------------------------------------

    category = "burglary"

    burglaries = find_by_category(category)

    print(f"\nFound {len(burglaries):,} '{category}' crimes.\n")

    print("First three burglary records:\n")

    for crime in burglaries[:3]:

        print(crime)

        print("-" * 50)

    # -------------------------------------------------------
    # Count by Category
    # -------------------------------------------------------

    print("\nCrime totals by category\n")

    category_counts = count_by_category()

    for row in category_counts:

        print(f"{row['_id']:<35} {row['count']:>5}")

    # -------------------------------------------------------
    # Update Crime Status
    # -------------------------------------------------------

    print("\n" + "=" * 60)
    print("TESTING UPDATE")
    print("=" * 60)

    first_crime = crimes[0]

    crime_id = str(first_crime["_id"])

    print(f"\nCrime ID: {crime_id}")

    print(
        f"Current review_status: "
        f"{first_crime.get('review_status', 'Not Set')}"
    )

    modified = update_crime_status(
        crime_id,
        "Pending Review"
    )

    print(f"\nDocuments updated: {modified}")

    updated = get_all_crimes()[0]

    print(
        f"New review_status: "
        f"{updated.get('review_status', 'Not Set')}"
    )

    # -------------------------------------------------------
    # Add Crime
    # -------------------------------------------------------

    print("\n" + "=" * 60)
    print("TESTING ADD")
    print("=" * 60)

    new_crime = {
        "category": "test-crime",
        "month": "2026-07",
        "location": {
            "latitude": "51.4545",
            "longitude": "-2.5879"
        },
        "review_status": "New"
    }

    inserted_id = add_crime(new_crime)

    print(f"\nNew crime inserted with ID: {inserted_id}")

    # -------------------------------------------------------
    # Delete Crime
    # -------------------------------------------------------

    print("\n" + "=" * 60)
    print("TESTING DELETE")
    print("=" * 60)

    deleted = delete_crime(inserted_id)

    print(f"\nDocuments deleted: {deleted}")

    # -------------------------------------------------------
    # Final Count
    # -------------------------------------------------------

    final_total = count_crimes()

    print(f"\nFinal crime count: {final_total:,}")

    print("\nCRUD testing complete.")


if __name__ == "__main__":
    main()