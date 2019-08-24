def sod(n):
    sum_ = 0
    while n > 0:
        sum_ += n%10
        n //= 10
    return sum_

for t in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    max_sod = 0
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            max_sod = max(max_sod, sod(A[i]*A[j]))
    print(max_sod)
