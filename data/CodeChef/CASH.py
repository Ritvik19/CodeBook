for t in range(int(input())):
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    print(sum(A) % k)