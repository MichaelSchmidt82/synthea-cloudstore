#!/bin/bash

MSG=/messages/synthea
CONFIG='synthea.properties'

touch $CONFIG
echo "exporter.baseDirectory = /output" >> $CONFIG

CSV="$(tr [A-Z] [a-z] <<< "$CSV")"
if [ "${CSV}" == "true" ]; then
  echo "Setting CSV options"
  echo "# CSV options" >> $CONFIG
  echo "exporter.csv.export = true" >> $CONFIG
fi

CCDA="$(tr [A-Z] [a-z] <<< "$CCDA")"
if [ "${CCDA}" == "true" ]; then
  echo "Setting CCDA options"
  echo "# CCDA options" >> $CONFIG
  echo "exporter.ccda.export = true" >> $CONFIG
fi

DSTU2="$(tr [A-Z] [a-z] <<< "$DSTU2")"
if [ "${DSTU2}" == "true" ]; then
  echo "Setting DSTU2 options"
  echo "# DSTU2 options" >> $CONFIG
  echo "exporter.fhir_dstu2.export = true" >> $CONFIG
  echo "exporter.hospital.fhir_dstu2.export = false" >> $CONFIG
  echo "exporter.practitioner.fhir_dstu2.export = false" >> $CONFIG
fi

STU3="$(tr [A-Z] [a-z] <<< "$STU3")"
if [ "${STU3}" == "true" ]; then
  echo "Setting STU3 options"
  echo "# STU3 options" >> $CONFIG
  echo "exporter.fhir_stu3.export = true" >> $CONFIG
fi

R4="$(tr [A-Z] [a-z] <<< "$R4")"
if [ "${R4}" == "true" ]; then
  echo "Setting R4 options"
  echo "# R4 options" >> $CONFIG
  echo "exporter.fhir.export = true" >> $CONFIG
  echo "exporter.fhir.bulk_data = false" >> $CONFIG
  echo "exporter.fhir.transaction_bundle = true" >> $CONFIG
  echo "exporter.hospital.fhir.export = false" >> $CONFIG
  echo "exporter.practitioner.fhir.export = false" >> $CONFIG
fi

if test -f "$MSG"; then
    echo "$MSG exists.  Skipping record generation"
else
    java -jar synthea-with-dependencies.jar -c $CONFIG -p $NUMBER_OF_RECORDS
    touch "$MSG"
fi