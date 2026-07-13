from database.crud import (
    count_crimes,
    get_all_crimes,
    find_by_category,
    count_by_category,
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


if __name__ == "__main__":
    main()