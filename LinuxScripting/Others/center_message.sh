#!/bin/bash
# Print message in center of terminal

# How many columns the terminal has.
cols=$( tput cols )

# How many lines (or rows) the terminal has.
rows=$( tput lines )

# Take all the command line arguments and assign them to a single variable message.
message=$@

# Find out how many characters are in the string message. We had to assign all the input values
# to the variable message first as ${#@} would tell us how many command line arguments
# there were instead of the number of characters combined.
input_length=${#message}

#know what 1/2 the length of the string message is in order to center it
half_input_length=$(( $input_length / 2 ))

middle_row=$(( $rows / 2 ))
middle_col=$(( ($cols / 2 ) - half_input_length ))

# Will clear the terminal.
tput clear

# Will place the cursor at the given row and column.
tput cup $middle_row $middle_col
# Will make everything printed to the screen bold.
tput bold
echo $@
# Will turn bold off (and any other changes we may have made).
tput sgr0
# Place the prompt at the bottom of the screen.
tput cup $( tput lines ) 0