import re
Regex_Pattern = r'^[a-z][123456789][^a-z][^A-Z][A-Z]'  # Do not delete 'r'.


print(str(bool(re.search(Regex_Pattern, input()))).lower())
