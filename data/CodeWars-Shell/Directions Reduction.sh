#!/bin/bash

before=$1

while true; do
    after=$(echo $before | sed -e 's/SN//g' -e 's/NS//g' -e 's/EW//g' -e 's/WE//g')
    if [ $after = $before ]; then
        break
    fi
    before=$after
done
    
echo $after