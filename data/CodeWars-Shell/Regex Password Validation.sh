password=$1
if [[
    ! "${password}" =~ ^[[:alnum:]]{6,}$ ||
    ! "${password}" =~ [[:digit:]] ||
    ! "${password}" =~ [[:lower:]] ||
    ! "${password}" =~ [[:upper:]]
]]; 
then
    echo "false"
else
    echo "true"
fi