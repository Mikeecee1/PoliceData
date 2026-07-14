# PoliceData

PoliceData is a small Python project that downloads street crime data from the UK Police API, stores it in MongoDB, and provides helper functions for reading and updating the data. The repository is organized into a simple pipeline: fetch data from the API, persist it in the database, and optionally build export or cloud-upload tooling around the stored records.

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [File Guide](#file-guide)
- [Setup](#setup)
- [Run](#run)
- [Tests](#tests)
- [Configuration](#configuration)

## Overview

The default workflow is:

1. Call the UK Police API for street crime data.
2. Insert the returned records into MongoDB.
3. Query, count, update, or delete records through the CRUD helpers.

The project currently includes a basic command-line entry point and a few script-style checks for database connectivity and CRUD behavior.

## Project Structure

```text
PoliceData/
├── app.py
├── config.py
├── requirements.txt
├── .env
├── README.md
├── api/
│   └── police_api.py
├── database/
│   ├── mongo.py
│   └── crud.py
├── export/
│   └── json_export.py
├── cloud/
│   └── s3_upload.py
├── exports/
└── tests/
```

## File Guide

- `app.py` is the main entry point. It downloads crime data and inserts it into MongoDB.
- `config.py` stores API defaults such as the base URL, coordinates, month, and request timeout.
- `api/police_api.py` contains the API client used to fetch crime records from the UK Police API.
- `database/mongo.py` creates the MongoDB connection from environment variables loaded through `.env`.
- `database/crud.py` contains the database helpers for inserting, reading, counting, filtering, updating, and deleting crime records.
- `test_connection.py` is a quick script for checking that the MongoDB collection connection works.
- `tests/test_crud.py` is a script-style CRUD check that exercises the database helper functions.
- `export/json_export.py` is currently an empty placeholder for JSON export logic.
- `cloud/s3_upload.py` is currently an empty placeholder for S3 upload logic.
- `exports/` is the output folder for generated export files.
- `requirements.txt` lists the Python dependencies needed by the project.
- `.env` should hold local configuration values such as MongoDB connection details.

## Setup

1. Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

2. Install the dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file with the MongoDB settings expected by `database/mongo.py`:

```env
MONGO_URI=your_mongo_connection_string
DATABASE_NAME=your_database_name
COLLECTION_NAME=your_collection_name
```

## Run

Run the main import-and-insert workflow:

```bash
python app.py
```

Check the MongoDB connection:

```bash
python test_connection.py
```

## Tests

The repository currently uses script-style checks rather than a full test runner.

Run the CRUD check script:

```bash
python tests/test_crud.py
```

If you later add automated unit tests, a common next step would be to run them with `pytest`.

## Configuration

The API defaults in `config.py` point to Bristol coordinates and a default month. You can change those values or pass different arguments to `get_crimes()` in `api/police_api.py` if you want data for another location or month.

MongoDB settings are read from environment variables in `database/mongo.py`, so local development depends on a correctly populated `.env` file.
