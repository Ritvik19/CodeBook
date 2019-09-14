for t in range(int(input())):
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    s = 0
    e = k
    sum_ = 0
    for i in range(k):
        sum_ += A[i]
    max_ = sum_
    while e < n:
        sum_ = sum_ - A[s] + A[e]
        s += 1
        e += 1
        if sum_ > max_:
            max_ = sum_
    print(max_)
