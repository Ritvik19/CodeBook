for t in range(int(input())):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    x = len(A)*max(A)-sum(A)
    if x == m:
        print("Yes")
    elif (m-x)%n == 0:
        print("Yes")
    else:
        print("No")
