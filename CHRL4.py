from functools import reduce
n, k = map(int, input().split())
A = [int(e) for e in input().split()]
product = A[-1]*A[0]
i = 1
while i < n-k:
    mnm = 100001
    min_i = 0
    for j,a in zip(range(k), A[i:min(i+k+1,n)]):
        if a < mnm:
            mnm = a
            min_i = i+j
    product *= mnm
    i = min_i + 1
    print(i)
print(product)
