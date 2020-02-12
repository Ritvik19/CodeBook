#!/bin/bash                                

diagonal() {                               
    num=$(( $1 + 1 ))                      
    den0=$(( $1 - $2 ))                    
    den1=$(( $2 + 1 ))                     

    max=$den0                              
    min=$den1                              

    if [ $den1 -gt $den0 ]                 
    then                                   
        max=$den1                          
        min=$den0                          
    fi                                     

    base=$(( $max + 1 ))                   

    num_res=$( seq -s "*" $base $num | bc )
    den_res=$( seq -s "*" 1 $min | bc )    
    res=$( echo "$num_res/$den_res" | bc ) 

    echo $res                              
}                                          

diagonal $1 $2  