ceil() {                                              
        echo "define ceil (x) {if (x/1 == x) {return x} \
        else { if (x<0) {return x/1 -1} \
        else {return x/1 + 1 }}} ; ceil($1)" | bc
}
wallpaper() {
    declare -a arr=("zero", "one", "two", "three", "four", "five", "six", "seven", 
                "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", 
                "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty")
    l=$1; w=$2; h=$3;
    r=$(bc <<< "scale=16; $l * $h * $w")
    r=$(ceil $r)
    if [[ "$r" -eq "0" ]]
    then
        r=0
    else
        r=$(bc <<< "scale=16; ($l * $h * 2 + $w * $h * 2) * 1.15 / 5.2")
        r=$(ceil $r)
    fi
    echo ${arr[$r]}
}
wallpaper $1 $2 $3