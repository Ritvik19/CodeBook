#!/bin/bash

if [ -z $1 ] ; then
    echo "Nothing to find!"
elif [ ! -d $1 ] ; then
    echo "Directory not found"
else
    echo "There are" `ls $1/ | wc -l` "files in" `cd $1; pwd`
fi