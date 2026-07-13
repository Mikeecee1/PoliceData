from api.police_api import get_crimes

from api.police_api import get_crimes
from database.crud import insert_crimes


def main():

    print("Downloading crime data...\n")

    crimes = get_crimes()

    print(f"Downloaded {len(crimes)} crime records.")

    print("\nSaving to MongoDB...")

    inserted = insert_crimes(crimes)

    print(f"Inserted {inserted} documents.")


if __name__ == "__main__":
    main()
    
# def main():

#     print("Downloading crime data...\n")

#     crimes = get_crimes()

#     print(f"Downloaded {len(crimes)} crime records.\n")

#     if crimes:
#         first = crimes[0]

#         print("First record")
#         print("-" * 40)

#         for key, value in first.items():
#             print(f"{key}: {value}")


# if __name__ == "__main__":
#     main()