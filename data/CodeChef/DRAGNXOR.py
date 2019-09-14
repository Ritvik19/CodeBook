for t in range(int(input())):
    n, a, b = map(int, input().split())
    na = bin(a).count('1')
    nb = bin(b).count('1')
    nxor = abs(n-na-nb)
    print((2**n)-(2**nxor))
