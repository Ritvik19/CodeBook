for t in range(int(input())):
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = [(k//a)*b for a, b in zip(A, B)]
    print(max(C))
