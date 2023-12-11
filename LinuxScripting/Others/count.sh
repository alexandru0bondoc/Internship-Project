#!/bin/bash

file=$1
sphrase=$2
grep -io $sphrase $file | wc -w
