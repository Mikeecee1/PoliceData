from api.police_api import get_crimes


def main():

    print("Downloading crime data...\n")

    crimes = get_crimes()

    print(f"Downloaded {len(crimes)} crime records.\n")

    if crimes:
        first = crimes[0]

        print("First record")
        print("-" * 40)

        for key, value in first.items():
            print(f"{key}: {value}")


if __name__ == "__main__":
    main()