#!/bin/bash

varpath=/usr/share/dict/words

if [ $# -ge 1 ]; then
	shuf "$varpath" | grep -owe "\\b\\w\\{${1}\\}\\b" | head -n 1

else
	shuf "$varpath" | head -n 1
fi
