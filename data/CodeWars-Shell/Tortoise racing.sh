#!/bin/bash
race() {
    v1=$1
    v2=$2
    g=$3
    v=$(( $v2-$v1 ))
    if [[ $v -le 0 ]];
    then
        echo "-1 -1 -1"
    else
        printf `echo "$g/$v" | bc`
        printf " "
        printf `echo "($g%$v*60/$v)" | bc`
        printf " "
        printf `echo "((($g%$v*60)%$v)*60/$v)" | bc`
    fi
}
race $1 $2 $3