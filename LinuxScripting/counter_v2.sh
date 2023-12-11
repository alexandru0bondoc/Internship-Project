#!/bin/bash

searchString=$1

shift

# Check if a search string and at least one file are provided
if [ -z "$searchString" ] || [ -z "$1" ]; then
    echo "Usage: $0 searchString file1 [file2 ...]"
    exit 1
fi

# Loop through each file provided as argument
for file in "$@"; do
    # Check if file exists
    if [ ! -f "$file" ]; then
        echo "File not found: $file"
        continue
    fi

    # Count occurrences and get line numbers
    echo "In file: $file"
    grep -n "$searchString" "$file" | while read -r line; do
        lineNumber=$(echo "$line" | cut -d: -f1)
        echo "Found at line: $lineNumber"
    done
    count=$(grep -c "$searchString" "$file")
    echo "Total occurrences in $file: $count"
    echo
done
