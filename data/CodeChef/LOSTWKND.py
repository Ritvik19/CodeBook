for t  in range(int(input())):
    *A, P = map(int, input().split())
    print("Yes") if sum(A)*P > 120 else print("No")