for t in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    n5, n10 = 0, 0
    flag = "YES"
    for a in A:
        if a == 5:
            n5 += 1
        elif a == 10:
            if n5 > 0:
                n5 -= 1
                n10 += 1
            else:
                flag = "NO"
                break
        else:
            if n10 > 0:
                n10 -= 1
            elif n5 > 1:
                n5 -= 2
            else:
                flag = "NO"
                break
    print(flag)