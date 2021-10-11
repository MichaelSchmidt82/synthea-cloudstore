FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

ENV GOOGLE_APPLICATION_CREDENTIALS="credentials.json"
ENV GCS_PATH='synthea'
ENV BUCKET_NAME='aou-curation-omop-dev_transfer_fhir'

COPY . .

CMD [ "python", "./entrypoint.py" ]