new_avg() {
    source_data="$1"
    source_avg=$2
    result=0
    result_r=ERROR
    j=1
    for i in $source_data;
    do
        i=$(echo 0 $i| awk '{printf("%.2f",$1+$2)}' )
        result=$(echo $result $i| awk '{printf("%.2f",$1+$2)}' )
        j=$((j+1))
    done
    source_r=$(echo $source_avg $j| awk '{printf("%.2f",$1*$2)}' )
    result_cp=$(echo " $source_r > $result "|bc)
    
    if [ Z$result_cp = "Z1" ];
    then
        result_r=$(echo "scale=0;($source_r-$result+0.90)/1"|bc)
        echo $result_r
    else 
        echo $result_r
    fi
}

new_avg "$1" $2