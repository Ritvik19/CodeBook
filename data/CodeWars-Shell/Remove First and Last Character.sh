function removeChar() {
  string=$1
  echo "${string:1:${#string}-2}"
}
removeChar $1