for i in range(int(input())):
    inp = input().split()
    N = int(inp[0])
    K = int(inp[1])
    S = int(inp[2])
    if K>N:
        print (-1)
        continue
    if (S>=7) and ((7*K)>(6*N)):
        print (-1)
        continue
    need = K*S
    ans = 0
    bought = 0
    while bought<K*S:
        bought += N
        ans += 1
    print (ans)
