#!/bin/bash
longest() {
    echo $1$2 | grep -o . | sort -u | paste -sd "" -
}
longest "$1" "$2"