#!/usr/bin/env bash

numPrimorial ()
{
    local -- numPrimes=$1
    count=$1
    n=100
    a=0
    result=1
    for((i=1;i<=n;i++))
    do
        for((x=1;x<=i;x++))
        do
            b=$(( $i%$x ))
            if [[ $b -eq 0 ]];
            then
                let a=$a+1
            fi
        done
        if [[ $a -eq 2 ]]; 
        then
            let result=$result*$i
            let count-=1
        fi
        a=0
        if [[ $count -eq 0 ]];
        then
            echo $result
            break
        fi
    done
}

numPrimorial $1