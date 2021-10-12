# Synthea-cloudstore
Generate and upload Synthea data to a cloud storage bucket

### Usage:
`docker-compose up`

### Configuration:

#### gs-etl
- `BUCKET_NAME`
    - A Google Cloud Storage bucket name.
- `GCS_PATH`
    - The path to store objects in `BUCKET_NAME`.

#### synthea
- NUMBER_OF_RECORDS
    - The number of records to generate.