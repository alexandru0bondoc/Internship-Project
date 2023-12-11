#!/bin/bash
# Basic arithmetic using expr

expr 5 + 4 
# basic format no quotes there must be spaces

expr "5 + 4"
#  If we do put quotes around the expression 
#  then the expression will not be evaluated but printed instead.

expr 5+4
# If we do not put spaces between the items 
# of the expression then the expression will not be evaluated but printed instead.

expr 5 \* $1

expr 11 % 2

a=$( expr 10 - 3 )
echo $a #7