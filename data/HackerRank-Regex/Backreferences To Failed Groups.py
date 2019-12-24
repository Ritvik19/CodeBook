import re
Regex_Pattern = r"^((\d\d-\d\d-\d\d-\d\d)|(\d{8}))$"  # Do not delete 'r'.


print(str(bool(re.search(Regex_Pattern, input()))).lower())
