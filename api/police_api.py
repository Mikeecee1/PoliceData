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
    lat=DEFAULT_LAT,
    lng=DEFAULT_LNG,
    month=DEFAULT_MONTH,
):
    """
    Retrieve street crime data from the UK Police API.

    Returns:
        list: List of crime records (dictionaries)

    Raises:
        requests.RequestException
    """

    url = f"{BASE_URL}/crimes-street/all-crime"

    params = {
        "lat": lat,
        "lng": lng,
        "date": month,
    }

    response = requests.get(
        url,
        params=params,
        timeout=REQUEST_TIMEOUT,
    )

    response.raise_for_status()

    return response.json()