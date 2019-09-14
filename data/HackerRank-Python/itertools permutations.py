# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
S, k = input().split()
for p in sorted(permutations(S, int(k))):
    print(''.join(p))
