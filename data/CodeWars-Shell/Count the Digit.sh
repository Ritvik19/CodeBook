#!/bin/bash
for k in `seq 0 $1`; do echo -n `expr $k * $k`; done | sed -e "s/[^$2]//g" | wc -c