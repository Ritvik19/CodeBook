for i in range(int(input())):
    n = int(input())
    A = [int(e) for e in input().split()]
    print(A.index(min(A))+1)
