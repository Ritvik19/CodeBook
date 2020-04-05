for t in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A = sum(A)- max(A)
    B = sum(B)- max(B)
    if A > B:
        print('Bob')
    elif B > A:
        print('Alice')
    else:
        print('Draw')