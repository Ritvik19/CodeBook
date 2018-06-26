for i in range(int(input())):
    n = int(input())
    A = [int(e) for e in input().split()]
    p1 =1
    p2 = p3 = 0
    if 5 in A:
        p2 = 1
    for marks in A:
        p3 += marks
        if marks <= 2:
            p1 = 0
    p3 /= n
    if p1 == 1 and p2 == 1 and p3 >= 4:
        print("Yes")
    else:
        print("No")
