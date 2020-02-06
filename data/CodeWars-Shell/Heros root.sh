int_rac () {
    n=$1
    x=$2
    i=1
    while : ; do
        diff=$(($x**2 - $n))
        absdiff=${diff#-}
        newguess=$(bc <<< "($x+$n/$x)/2")
        if [[ "$absdiff" -le 1 || "$newguess" -eq "$x" ]]; then
            break
        fi
        x=$newguess
        ((i++))
    done
    echo "$i"
}
int_rac "$1" "$2"