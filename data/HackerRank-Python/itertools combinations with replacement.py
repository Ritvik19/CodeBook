from itertools import combinations_with_replacement

sr, kr = input().split(' ')
s = sorted(list(sr))
k = int(kr)

for i in combinations_with_replacement(s,k):
    print(''.join(i))
