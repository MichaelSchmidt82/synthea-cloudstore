# Synthea-cloudstore
This Docker stack will generate and upload synthetic health record data to a Google Cloud Storage bucket.
- `gs-etl` is the loader process used to load data to a Google Cloud Storage bucket.  It requires a service account access key (credentials.json). Instructions on obtaining credentials are available [here](https://cloud.google.com/iam/docs/creating-managing-service-account-keys).
- `synthea` generates synthetic health record data.

## Usage:
`docker-compose up`

## Configuration options:

### gs-etl
- `BUCKET_NAME`
    - A Google Cloud Storage bucket name.  The bucket must exist prior to execution.
- `GCS_PATH`
    - The path to store objects in `BUCKET_NAME`.  The path will be created if it doesn't exist.

### synthea

- NUMBER_OF_RECORDS
    - The number of records to generate.
- CSV
    - Export raw CSVs.  The CSVs will be stored in a folder labeled "csv".
- CCDA
    - Export in CCDA format.  The output files follow the R4 format specification and are placed in a folder labeled "ccda".
- DTSU2
    - Export in DSTU2 format.  Files are stored in a folder labeled "fhir_dstu2".
- STU3
    - Export in STU3 format.  Files are stored in a folder labeled "fhir_stu3".
- R4
    - Export in R4 format.  Files are stored in a folder labeled "fhir".