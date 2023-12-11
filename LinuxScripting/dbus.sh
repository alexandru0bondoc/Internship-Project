#!/bin/bash
# Dbus monitor status battery change

sudo dbus-monitor --system | grep -A 1 "string \"OnBattery\"" |
while read -r line
do
    if [[ ${line} == *"boolean"* ]]; then
        status=$(echo $line | awk '{print $3}')
        if [[ $status == "true" ]]; then
            echo "This machine is currently using the battery"
        else
            echo "This machine is currently plugged in"
        fi
    fi
done