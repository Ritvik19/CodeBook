def fib_check(perm):
    for i in range(2, len(perm)):
        if perm[i] != perm[i-1] + perm[i-2]:
            return False
    return True

for t in range(int(input())):
    string = list(input())
    dct = {}
    for s in string:
        if s not in dct.keys():
            dct[s] = 1
        else:
            dct[s] += 1
    perm = list(sorted(dct.values()))
    if len(perm) < 3:
        print("Dynamic")
    elif len(perm) >= 3:
        if len(perm) >= 4 and perm[3] != perm[2] + perm[1]:
            perm[0], perm[1] = perm[1], perm[0]
        if fib_check(perm) == True:
            print("Dynamic")
        else:
            print("Not")
