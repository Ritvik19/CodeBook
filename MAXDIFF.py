for t in range(int(input())):
    n, k = map(int, input().split())
    W = [int(e) for e in input().split()]
    W = sorted(W)
    if n-k < k:
        k = n-k
    son = W[:k]
    chef = W[k:]
    print(sum(chef)-sum(son))
