import re

print(';'.join(sorted(set([i.group(2) for i in re.finditer(
    r'https?://(www2?\.)?(([A-Za-z0-9-]+\.)+[A-Za-z0-9]+)', '\n'.join(input() for _ in range(int(input()))))]))))
