a=$1
b=$2
c=$3
ARRAY=($((a * b * c)) $((a * (b + c))) $(((a + b) * c)) $((a + b + c)))

max=0
for v in ${ARRAY[@]};
do
    if (( $v > $max )); 
    then 
        max=$v
    fi
done
echo $max