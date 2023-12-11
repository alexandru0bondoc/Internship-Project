#!/bin/bash

# Setting the right files 
fisier_selector='./bashcrc.txt'
fisier_target='./bashcrc'

# Setting keys and initializing values
keys=("ARTIFACTORY_API_KEY" "ARTIFACTORY_USER" "ANDROID_HOME" "JAVA_HOME" "IVI_ADB_SERIAL")
values=()

# Check to see if the files exists and are not empty 
if [ ! -s ${fisier_selector} ];then
	echo "The ${fisier_selector} it doesn't exist or it's empty"
	exit 1
elif [ ! -s ${fisier_target} ];then
	echo "The ${fisier_target} it doesn't exist or it's empty"
	exit 1
fi

# Extract the only interesting lines from the selector file
# Extract only the specific value of the line
# Populate the values array
for key in ${keys[@]}
do
	line=$( grep "${key}" "${fisier_selector}" )
	value=$( echo ${line} | cut -d '=' -f2 )
	values+=("${value} ")
done

# Iterate over the keys and replace the values in fisier_target
for ((i=0; i<${#keys[@]}; i++)); do
# Remove any trailing spaces from values
    selector_value=$(echo "${values[i]}" | xargs)

# Use sed to replace the value in fisier_target after the key=
# -i option edits the file in place
# The pattern looks for 'key=' and replaces anything that follows it with the new value
# The part before 'key=' is preserved using a capturing group
# Avoids any comment lines that start with #
	sed -i "/^#/!s|\(${keys[i]}=\).*|\1${selector_value}|" "${fisier_target}"
done

