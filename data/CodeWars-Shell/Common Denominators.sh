gcd () {
    local m=$1
    local n=$2
    local r
    while :; 
    do
        r=$((m % n))
        ((r != 0)) || break
        m=$n
        n=$r
    done
    echo "$n"
}

lcm () {
    local m=$1
    local n=$2
    local gcd
    gcd=$(gcd "$m" "$n")
    echo $((m / gcd * n))
}

reduce () {
    local n
    local d
    read -r n d <<<"$1"
    local gcd
    gcd=$(gcd "$n" "$d")
    echo "$((n / gcd)) $((d / gcd))"
}

read_fractions () {
    local varname=$1
    shift
    while [ "$#" -gt 1 ]; do
        eval "$varname"'+=("$(reduce "$1 $2")")'
        shift 2
    done
}

lcm_multi () {
    local lcm=1
    local x
    for x in "$@"; do
        lcm=$(lcm "$lcm" "$x")
    done
    echo "$lcm"
}

denominators () {
    local frac n d
    for frac in "$@"; do
        cut -d' ' -f2 <<<"$frac"
    done
}

expand () {
    local D=$1
    local n d
    read -r n d <<<"$2"
    echo "$((D / d * n)) $D"
}

IFS=, read -r -a parts <<<"$1"

fractions=()
read_fractions fractions "${parts[@]}"

D=$(lcm_multi $(denominators "${fractions[@]}"))
result=()
for frac in "${fractions[@]}"; do
    result+=("$(expand "$D" "$frac")")
done

echo "${result[*]}"