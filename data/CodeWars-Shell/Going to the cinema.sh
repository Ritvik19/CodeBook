#!/bin/bash
#!/bin/bash
card=$1
ticket=$2
perc=$3
n=0
system_a=0
system_b=$card
while ([ $(printf %.0f $(bc<<<"$system_b+0.5")) -ge $system_a ])
do
    n=$(( $n + 1 ))
    system_a=$((system_a+ticket))
    system_b=$( bc <<< "scale=8; $system_b + $ticket * $perc ^ $n / 1" )
done
echo $n