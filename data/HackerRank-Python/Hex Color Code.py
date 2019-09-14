import re
HEX_REGEX = re.compile(r"#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})(;|,|\))")
matches = []
for i in range(int(input())):
    matches += HEX_REGEX.findall(input())
for m in matches:
    print('#'+m[0])
