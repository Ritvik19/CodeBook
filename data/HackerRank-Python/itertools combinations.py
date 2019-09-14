# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
S, k = input().split()
S = list(S)
S.sort()
for i in range(1,int(k)+1):
    for p in sorted(list(combinations(S, i))):
        print(''.join(p))
