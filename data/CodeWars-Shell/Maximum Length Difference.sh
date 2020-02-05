#!/bin/bash
# input : 2 strings with substrings separated by `,`
# output: number as a string
accum () {
  IFS=','
  read -ra arr1 <<<"$1"
  read -ra arr2 <<<"$2"
  max=-1
  diff=-1
  for i in "${arr1[@]}"
  do
    for j in "${arr2[@]}"
    do
        l1=`echo "${#i}"`
        l2=`echo "${#j}"`
        ((diff=l1-l2))
        diff=`echo ${diff#-}`
        if [[ diff -gt max ]];
        then
          max=$diff
        fi
    done
  done
  echo $max
}
accum "$1" "$2"