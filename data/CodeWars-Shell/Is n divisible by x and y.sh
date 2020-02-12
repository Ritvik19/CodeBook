#!/bin/bash
n=$1
x=$2
y=$3
if [[ $n%$x -eq 0 && $n%$y -eq 0 ]];
then
    echo "true"
else
    echo "false"
fi