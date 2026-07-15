BASE_URL = "https://data.police.uk/api"

DEFAULT_LAT = 51.4545      # Bristol
DEFAULT_LNG = -2.5879

DEFAULT_MONTH = "2025-12"

REQUEST_TIMEOUT = 10  # seconds

#crime categories to export to json file for s3 upload
EXPORT_CATEGORIES = [   
    "burglary",
    "violent-crime",
    "vehicle-crime",
]