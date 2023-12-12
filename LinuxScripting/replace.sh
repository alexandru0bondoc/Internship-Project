#!/bin/bash

inputFile="./log.txt"
outputFile="replacement_log.txt"

luckyWord="AUTOMATION"

for i in {63..72}; do
# Keep evidence - index for the replacement letter
    index=$((i-63))

# Extract the 6th word from the line
    originalWord=$(sed -n "${i}p" "${inputFile}" | awk '{print $6}')
    
# Extract the letter from the luckyWord
    letter=$(echo ${luckyWord} | cut -c$((index+1)))

# Replace the 6th word with "AUTOMATION" in the line
    sed -i "${i}s/\b$originalWord\b/${letter}/" "${inputFile}"

    echo "$originalWord was replaced with the letter: $letter" >> "${outputFile}"
done
