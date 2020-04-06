for t in range(int(input())):
    n = int(input())
    S = list(map(int, input().split()))
    threshold = S[0]
    sum = S[0]
    for i in range(1, n):
        threshold = min(threshold, S[i])
        sum += threshold
    print(sum)