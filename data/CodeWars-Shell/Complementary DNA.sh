#!/bin/sh
string=$1
string=`echo ${string//"A"/"1"}`
string=`echo ${string//"T"/"2"}`
string=`echo ${string//"C"/"3"}`
string=`echo ${string//"G"/"4"}`
string=`echo ${string//"1"/"T"}`
string=`echo ${string//"2"/"A"}`
string=`echo ${string//"3"/"G"}`
string=`echo ${string//"4"/"C"}`
echo $string