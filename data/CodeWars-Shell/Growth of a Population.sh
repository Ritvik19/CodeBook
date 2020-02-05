#!/bin/bash
nbYear() {
    nb_year=0
    p0=$1
    percentage=$2
    aug=$3
    p=$4
    while [ $p0 -lt $p ];
    do
        p0=`echo "p0=$p0+$p0*$percentage/100;p0" | bc`
        ((p0=$p0+$aug))
        ((nb_year=$nb_year+1))
    done
    echo $nb_year
}

nbYear $1 $2 $3 $4