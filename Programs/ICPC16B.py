for t in range(int(input())):
    n = int(input())
    A = [int(e) for e in input().split()]
    one, zero, negone = A.count(1), A.count(0), A.count(-1)
    other = n-(one + zero + negone)
    if other >= 2:
        print("no")
    elif negone >= 1 and other == 1:
        print("no")
    elif negone >= 2 and one == 0:
        print("no")
    else:
        print("yes")
