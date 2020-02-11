base=$1
factor=$2
if [[ $base%$factor -eq 0 ]];
then
    echo true
else
    echo false
fi