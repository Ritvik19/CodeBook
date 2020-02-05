#!/bin/bash

if [ $# -eq 0 ];
then
    echo "Nothing to find"
else
    if [ -e $1 ];
    then
        echo "Found $1"
    else
        echo "Can't find $1"
    fi
fi  