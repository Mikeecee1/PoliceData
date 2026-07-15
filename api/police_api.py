# api/police_api.py

import requests

from config import (
    BASE_URL,
    DEFAULT_LAT,
    DEFAULT_LNG,
    DEFAULT_MONTH,
    REQUEST_TIMEOUT,
)


def get_crimes(
    latitude=DEFAULT_LAT,
    longitude=DEFAULT_LNG,
    month=DEFAULT_MONTH,
):
    """
    Retrieve street crime data from the UK Police API.

    Args:
        latitude (float): Latitude of the search location.
        longitude (float): Longitude of the search location.
        month (str): Month in YYYY-MM format.

    Returns:
        list: List of crime records (dictionaries).

    Raises:
        requests.RequestException: If the API request fails.
    """

    url = f"{BASE_URL}/crimes-street/all-crime"

    params = {
        "lat": latitude,
        "lng": longitude,
        "date": month,
    }

    response = requests.get(
        url,
        params=params,
        timeout=REQUEST_TIMEOUT,
    )

    response.raise_for_status()

    return response.json()