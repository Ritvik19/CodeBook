#!/bin/bash
res=$1
i=0
while [[ "$res" < "$2" ]];do
    res=$( echo "$res * (1+ $3/36000)" | bc -l)
    let i++
done
date -d "2016-01-01 $i days" +%Y-%m-%d