from collections import namedtuple
n = int(input())
heads = input()
x = namedtuple('record', heads)
records = []
for i in range(n):
    _ = list(map(lambda x: x.strip(), input().split()))
    records.append(x(*_))
total = 0
for r in records:
    total += int(r.MARKS)
print(total/n)
