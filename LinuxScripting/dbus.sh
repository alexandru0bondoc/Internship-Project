#!/bin/bash

while :
do
STATE=$(sudo dbus-send --system --print-reply --dest=org.freedesktop.UPower /org/freedesktop/UPower/devices/DisplayDevice org.freedesktop.DBus.Properties.Get string:"org.freedesktop.UPower.Device" string:"State")
value=$(echo ${STATE} | awk '{print $NF}')
case "$value" in
	*1*)
	echo "This machine is currently plugged in"
	;;
	*2*)
	echo "This machine is currently using the battery"
	;;
esac
done