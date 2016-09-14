#!/bin/bash

if [ -e fibs.csv ]; then #check if fibs.csv already exists
    if [ -e fibs.csv.bak ]; then #check if the backup file already exists
        echo 'Error: backup files fibs.csv.bak already exists. Aborting.'
        exit 1
    else #if backup file doesn't exist
        mv fibs.csv fibs.csv.bak
        echo 'fibs.csv has been backed up to fibs.csv.bak'
    fi
fi

for n in $(seq 10000); do   # this takes a while
    ./fib.py $n >> fibs.csv # append number (and newline) to file
    truncate -s -1 fibs.csv # truncate off that newline character
    printf "," >> fibs.csv  # append a comma
done
truncate -s -1 fibs.csv # remove the comma at the end
