#!/bin/bash

searchString=$1
file=$2

# Check if both arguments are provided
if [ "$#" -ne 2 ]; then
    echo "Usage: ${0} searchString file"
    exit 1
fi

# Count occurrences
count=$(grep -o "${searchString}" "${file}" | wc -l)

# Output the result
echo "The string '${searchString}' occurs ${count} times in ${file}."
