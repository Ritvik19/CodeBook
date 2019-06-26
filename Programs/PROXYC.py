from math import ceil
for t in range(int(input())):
    d = int(input())
    S = input()
    threshold= ceil(0.75*d)
    required = threshold-S.count('P')
    possible_proxies = 0
    for i in range(2, d-2):
        if S[i] == 'A' and (S[i-1] == 'P' or S[i-2] == 'P') and (S[i+1] == 'P' or S[i+2] == 'P'):
            possible_proxies += 1
    if possible_proxies >= required:
        print(max(required,0))
    else:
        print(-1)
