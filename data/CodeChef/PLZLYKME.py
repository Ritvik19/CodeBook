for t in range(int(input())):
    l, d, s, c = map(int, input().split())
    flag = 0
    if s >= l:
        print("ALIVE AND KICKING")
        flag = 1
        continue
    for i in range(d-1):
        s *= c+1
        if s >= l:
            flag = 1
            break
    if flag == 1:
        print("ALIVE AND KICKING")
    else:
        print("DEAD AND ROTTING")
