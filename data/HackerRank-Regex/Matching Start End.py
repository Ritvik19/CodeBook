import re
Regex_Pattern = r"^\d\w\w\w\w\.$"  # Do not delete 'r'.


print(str(bool(re.search(Regex_Pattern, input()))).lower())
