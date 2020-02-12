#!/bin/bash
fun(){
    if (( $(echo "$1 <= 0" | bc -l) ));
    then
        echo "None"
    else
        thickness=0.0001
        times=0
        while (( $(echo "$thickness < $1" | bc -l) ));
        do
            times=`echo "$times + 1" | bc`
            thickness=`echo "$thickness * 2" | bc`
        done
        echo $times
    fi
}
fun $1