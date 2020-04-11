for t in range(int(input())):
    n, c = map(int, input().split())
    A = list(map(int, input().split()))
    if c >= sum(A):
        print("Yes")
    else:
        print("No")
