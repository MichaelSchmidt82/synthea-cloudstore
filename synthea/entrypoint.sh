#!/bin/sh
FILE=/messages/synthea

if test -f "$FILE"; then
    echo "$FILE exists.  Skipping record generation"
else
    java -jar synthea-with-dependencies.jar -c /synthea.properties -p $NUMBER_OF_RECORDS
    touch "$FILE"
fi
