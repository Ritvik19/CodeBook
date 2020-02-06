#!/bin/bash
seven () {
    bc <<< "
    scale=0
    counter=0
    m=$1
    while( m > 99 ) {
        counter = counter + 1
        x = m / 10
        y = m % 10
        m = x - 2 * y
    }
    print m, \", \", counter
    "
}
seven "$1"