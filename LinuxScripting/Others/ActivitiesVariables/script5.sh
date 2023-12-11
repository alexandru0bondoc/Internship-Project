#!/bin/bash

if [ $# -ge 1 ]; then
	base_filename=$(basename "$1")
	extension="${base_filename##*.}"
	base_filename="${base_filename%.*}"
	filename="${base_filename}_$(date '+%Y-%m-%d').${extension}"
	if cp "${1}" "${filename}"; then
		echo "File copied to $filename"
	else
		echo "Error: Failed to copy the file"
	fi
else
	echo "The file argument wasn't provided!"
fi
