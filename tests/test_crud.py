from unittest import result

from database.crud import (
    count_crimes,
    get_all_crimes,
    find_by_category,
    count_by_category, 
    update_crime_status,
    delete_crime, 
)


def main():

    print("=" * 50)
    print("CRUD FUNCTION TESTS")
    print("=" * 50)

    # -----------------------------------
    # Count crimes
    # -----------------------------------

    total = count_crimes()

    print(f"\nTotal crimes: {total:,}")

    # -----------------------------------
    # Get all crimes
    # -----------------------------------

    crimes = get_all_crimes()

    print(f"\nRetrieved {len(crimes):,} documents.")

    print("\nFirst document:\n")

    print(crimes[0])

    # -----------------------------------
    # Find by category
    # -----------------------------------

    category = "burglary"

    burglaries = find_by_category(category)

    print(f"\nFound {len(burglaries):,} '{category}' crimes.")

    # Show first three

    print("\nSample results:\n")

    for crime in burglaries[:3]:

        print(crime)

        print("-" * 40)

    # -----------------------------------
    # Count by category
    # -----------------------------------

    print("\nCrime totals by category\n")

    counts = count_by_category()

    for row in counts:

        print(f"{row['_id']:<35} {row['count']:>5}")

    #-----------------------------------
    # Update a crime status 
    #-----------------------------------
    # crimes = get_all_crimes()

    # crime = crimes[0]

    # crime_id = str(crime["_id"])

    # print(f"\nTesting update")

    # modified = update_crime_status(
    #     crime_id,
    #     "Reviewed"
    # )

    # print(f"Documents updated: {modified}")

    # updated = get_all_crimes()[0]

    # print(updated.get("review_status"))
    print("\n" + "=" * 50)
    print("TESTING UPDATE")
    print("=" * 50)

    crimes = get_all_crimes()

    crime = crimes[0]

    crime_id = str(crime["_id"])

    print(f"\nCrime ID: {crime_id}")

    print(f"Current review_status: {crime.get('review_status', 'Not Set')}")

    result = update_crime_status(
    crime_id,
    "Pending Review"
    )

    print(f"\nMatched documents : {result.matched_count}")
    print(f"Modified documents: {result.modified_count}")

# Read the document back from MongoDB

    updated = get_all_crimes()[0]

    print(
        f"\nNew review_status: "
        f"{updated.get('review_status', 'Not Set')}"
    )


    #Test error handling for invalid id
    # modified = update_crime_status(
    # "NotAValidObjectId",
    # "Reviewed"
    # )
    # print(modified)


if __name__ == "__main__":
    main()