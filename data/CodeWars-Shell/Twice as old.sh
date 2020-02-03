dad_years_old=$1
son_years_old=$2

diff=$((2*son_years_old-dad_years_old))
echo ${diff#-}
exit