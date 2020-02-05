#!/bin/bash
limit=$3
factor1=$1
factor2=$2
for ((i=1; i<=$3; i+=1));
do
    if [ $(($i%$factor1)) -eq 0 ] && [ $(($i%$factor2)) -eq 0 ];
    then
        echo $i
    fi
done