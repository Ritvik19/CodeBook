month="$1"
month=`echo "$month" | tr '[:upper:]' '[:lower:]'`
month=`echo ${month:0:3}`
case "$month" in
        jan) MON=01 ;;
        feb) MON=02 ;;
        mar) MON=03 ;;
        apr) MON=04 ;;
        may) MON=05 ;;
        jun) MON=06 ;;
        jul) MON=07 ;;
        aug) MON=08 ;;
        sep) MON=09 ;;
        oct) MON=10 ;;
        nov) MON=11 ;;
        dec) MON=12 ;;
esac

echo $MON