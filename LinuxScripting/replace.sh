#!/bin/bash

inputFile="./log.txt"
outputFile="replacement_log.txt"

for i in {63..69}; do
    # Extract the 6th word from the line
    originalWord=$(sed -n "${i}p" "$inputFile" | awk '{print $6}')
    
    # Replace the 6th word with "AUTOMATION" in the line
    sed -i "${i}s/\b$originalWord\b/AUTOMATION/" "$inputFile"

    echo "$originalWord was replaced with the letter: [A, U, T, O, M, A, T, I, O, N]" >> "$outputFile"
done
