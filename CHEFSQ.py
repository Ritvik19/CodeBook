for i in range(int(input())):
    seql = int(input())
    seq = [int(e) for e in input().split(" ")]
    sbsql = int(input())
    sbsq = [int(e) for e in input().split(" ")]
    if sbsq in seq:
        print("Yes")
    else:
        print("No")
