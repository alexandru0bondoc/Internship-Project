#!/bin/bash
# case example

case $1 in
	start)
		echo starting
		;;
#We identify the end of this set of statements with a double semi-colon ( ;; ). 
#Following this is the next case to consider.
	stop)
		echo stoping
		;;
	restart)
		echo restarting
		;;
	*)
		echo don\'t know
		;;
esac
#esac is case backwards and indicates we are at the end of the case statement. 
#Any other statements after this will be executed normally.