#!/bin/bash
gps() {
    echo $2 | tr "," "\n" | awk "BEGIN{max=0}
    {if(NR!=1 && \$1-n>max){max=\$1-n}};
    {n=\$1};
    END{print max * 3600 / $1}"
}
gps $1 "$2"