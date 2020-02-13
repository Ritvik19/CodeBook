#!/bin/bash
bouncingBall() {
    h=$1; bounce=$2;window=$3; rebounds=-1
    c1=$(echo "$h > $window" | bc)
    c2=$(echo "$h > 0" | bc)
    c3=$(echo "$bounce < 1.0" | bc)
    c4=$(echo "$bounce > 0.0" | bc)
    cond=$(($c1 * $c2 * $c3 * $c4))
    if [ $cond -eq 1 ]
    then 
        while (( $(echo "$h > $window" | bc -l) ))
        do
            rebounds=$((rebounds+2))
            h=$(bc <<< "scale=8; $bounce * $h")
        done
    fi
    echo $rebounds
}
bouncingBall $1 $2 $3