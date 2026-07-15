


def recommend_category(counts):
    """
    Recommend the crime category with the highest frequency.

    Args:
        counts (list): Output from count_by_category().

    Returns:
        dict | None: Recommended category record, or None if no data.
    """

    if not counts:
        return None

    return counts[0]


def show_recommendation(counts):
    """
    Display a recommendation based on the downloaded dataset.

    Args:
        counts (list): Output from count_by_category().
    """

    recommendation = recommend_category(counts)

    if recommendation is None:

        print("\nNo recommendation available.")

        return None

    total_crimes = sum(row["count"] for row in counts)

    percentage = (
        recommendation["count"] / total_crimes
    ) * 100

    crime = (
        recommendation["_id"]
        .replace("-", " ")
        .title()
    )

    print("\n" + "=" * 60)
    print("RECOMMENDATION")
    print("=" * 60)

    print(
        f"\n{crime} is the most common crime "
        f"in this dataset."
    )

    print(
        f"\n{recommendation['count']:,} incidents "
        f"({percentage:.1f}% of all recorded crimes)"
    )

    print(
        f"\nRecommendation:"
        f"\nExport '{crime}' for further analysis."
    )

    return recommendation["_id"]

    
       