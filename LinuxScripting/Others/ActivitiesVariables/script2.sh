#!/bin/bash

varpath=/usr/share/dict/words

cat $varpath | shuf | head -n 1
cat $0