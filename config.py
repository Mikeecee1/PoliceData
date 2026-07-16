BASE_URL = "https://data.police.uk/api"

DEFAULT_LAT = 51.4545      # Bristol
DEFAULT_LNG = -2.5879

DEFAULT_MONTH = "2025-12"

LOCATIONS = {
    "1": {
        "name": "Bristol",
        "latitude": 51.4545,
        "longitude": -2.5879,
    },
    "2": {
        "name": "Bath",
        "latitude": 51.3813,
        "longitude": -2.3590,
    },
    "3": {
        "name": "Cardiff",
        "latitude": 51.4816,
        "longitude": -3.1791,
    },
    "4": {
        "name": "Leeds",
        "latitude": 53.8008,
        "longitude": -1.5491,
    },
    "5": {
        "name": "Manchester",
        "latitude": 53.4822,
        "longitude": -2.2426,
    },
    "6": {
        "name": "Birmingham",
        "latitude": 52.4862,
        "longitude": -1.8904,
    }

}

AVAILABLE_MONTHS = [
    "2025-12",
    "2025-11",
    "2025-10",
    "2025-09",
    "2025-08",
    "2025-07",
]

REQUEST_TIMEOUT = 10  # seconds

#crime categories to export to json file for s3 upload
EXPORT_CATEGORIES = [   
    "burglary",
    "violent-crime",
    "vehicle-crime",
]