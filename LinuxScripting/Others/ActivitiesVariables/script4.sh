#!/bin/bash

if [ $# -ge 1 ]; then
	filename="$(date '+%Y-%m-%d')_$1"
	if cp "$1" "$filename"; then
		echo "File copied to $filename"
	else
		echo "Error: Failed to copy the file"
	fi
else
	echo "The file argument wasn't provided!"
fi
