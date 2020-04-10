for t in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    a = [ele * 2 for ele in A]
    xor = 0
    for i in a:
        xor ^= i
    print(xor)