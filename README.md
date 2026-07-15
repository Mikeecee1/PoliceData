# PoliceData – Python ETL Pipeline

## Project Summary

PoliceData is a Python ETL (Extract, Transform, Load) application that retrieves street crime data from the [UK Police API](https://data.police.uk/docs/), stores it in MongoDB, transforms selected records into JSON, and uploads the results to an AWS S3 bucket.

The application provides an interactive command-line interface that allows users to:

* Select a location and month to download crime data.
* Store data in a user-defined MongoDB collection.
* Analyse crime categories within the downloaded dataset.
* Select crime categories for export.
* Generate JSON files with meaningful filenames.
* Optionally upload the exported data to AWS S3.

The project demonstrates a complete cloud ETL workflow using Python, MongoDB, AWS S3 and REST APIs.


## Table of Contents

- [Project Summary](#project-summary)
- [Overview](#overview)
- [ETL Workflow](#etl-workflow)
- [Project Structure](#project-structure)
- [Features](#features)
- [File Guide](#file-guide)
- [Setup](#setup)
- [Run](#run)
- [Tests](#tests)
- [Technologies](#technologies)
- [Configuration](#configuration)
- [Future Improvements](#future-improvements)
- [Collaborators](#collaborators)

## Overview

The application follows a complete ETL workflow.

1. The user selects a location and month.
2. Crime data is downloaded from the UK Police API.
3. Records are stored in a MongoDB collection chosen by the user.
4. Crime statistics are generated from the imported dataset.
5. The user selects which crime category to export.
6. Selected records are transformed into a simplified JSON format.
7. The JSON file is optionally uploaded to AWS S3.


## ETL Workflow

```text
                 UK Police API
                       │
                       ▼
                Extract Crime Data
                       │
                       ▼
                  MongoDB Database
                       │
                       ▼
             Analyse Crime Categories
                       │
                       ▼
              Transform Selected Data
                       │
                       ▼
                  JSON Export File
                       │
                       ▼
                  AWS S3 Bucket
```



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
## Features

* Interactive command-line interface.
* Download crime data from the UK Police API.
* User-selectable locations and months.
* Dynamic MongoDB collection creation.
* Full CRUD operations for MongoDB.
* Crime category analysis using MongoDB aggregation.
* JSON export with data transformation.
* Optional upload to AWS S3.
* Modular project structure with separate API, database, export, cloud and UI modules.


## File Guide

- `app.py` is the main entry point. It downloads crime data and inserts it into MongoDB.
- `config.py` stores API defaults such as the base URL, coordinates, month, and request timeout.
- `api/police_api.py` contains the API client used to fetch crime records from the UK Police API.
- `database/mongo.py` creates the MongoDB connection from environment variables loaded through `.env`.
- `database/crud.py` contains the database helpers for inserting, reading, counting, filtering, updating, and deleting crime records.
- `test_connection.py` is a quick script for checking that the MongoDB collection connection works.
- `tests/test_crud.py` is a script-style CRUD check that exercises the database helper functions.
- `tests/test_export.py` runs the JSON export flow and prints the output file path and exported count.
- `tests/test_upload.py` runs the S3 upload flow for the exported JSON file.
- `export/json_export.py` transforms stored crime records and writes them to `exports/transformed_crimes.json`.
- `cloud/s3_upload.py` uploads a local file to S3 using AWS credentials and bucket settings from the environment.
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


## Tests

The repository currently uses script-style checks rather than a full test runner.

Run the CRUD check script:

```bash
python -m tests/test_crud.py
```

Run the export check script:

```bash
python -m tests/test_export.py
```

Run the upload check script:

```bash
python -m tests/test_upload.py
```

Check the MongoDB connection:

```bash
python -m tests/test_connection.py
```
## Technologies

* Python 3
* MongoDB
* PyMongo
* REST APIs
* Requests
* AWS S3
* Boto3
* JSON
* Git & GitHub


## Configuration

## Configuration

The application uses a combination of **`config.py`** and **environment variables** stored in **`.env`**.

### `config.py`

`config.py` contains application defaults and user-selectable options, including:

* UK Police API base URL.
* Default latitude and longitude.
* Default month.
* Predefined locations displayed in the application menu.
* Available months for download.
* API request timeout.

Additional locations or months can be added by updating the dictionaries and lists in `config.py` without modifying the application logic.

### `.env`

Sensitive configuration values are stored in a local `.env` file and are not committed to source control.

Example:

```env
MONGO_URI=mongodb://localhost:27017
DATABASE_NAME=PoliceData
COLLECTION_NAME=CrimeData

AWS_PROFILE=your-profile
AWS_REGION=your-region-1
S3_BUCKET=your-s3-bucket
```

These values are used to:

* Connect to MongoDB.
* Select the default MongoDB collection (when one is not provided by the application).
* Authenticate with AWS.
* Upload exported JSON files to Amazon S3.


## Future Improvements

Possible future enhancements include:

* Support for downloading multiple locations in a single run.
* Support for downloading multiple months.
* Recommendation system suggesting crime categories for export.
* Interactive dashboards and visualisations.
* Automated scheduling of ETL jobs.
* Semantic search over richer crime datasets using embeddings or Retrieval-Augmented Generation (RAG).

### Collaborators


