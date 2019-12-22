import re
Regex_Pattern = r'^[^0-9][^aeiou][^bcDF]\S[^AEIOU][^.,]$'  # Do not delete 'r'.


print(str(bool(re.search(Regex_Pattern, input()))).lower())
