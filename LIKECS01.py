for t in range(int(input())):
    S = input()
    flag = 0
    for s in S:
        if S.count(s) >= 2:
            print("yes")
            flag = 1
            break
    if flag == 0:
        print("no")
