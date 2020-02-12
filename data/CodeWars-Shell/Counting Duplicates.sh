#!/bin/bash
echo $1 \
    | tr '[:upper:]' '[:lower:]' \
    | awk -F '' 'BEGIN{OFS="\n"} {$1=$1; print $0}' \
    | sort \
    | uniq -c \
    | awk '{if ($1>=2) print $2}' \
    | wc -l