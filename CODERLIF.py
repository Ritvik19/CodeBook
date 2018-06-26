for t in range(int(input())):
    work = [int(e) for e in (input().split())]
    flag = flag2 = count = 0
    for w in work:
        if flag == 0:
            if w == 1:
                flag = 1
                count += 1
        elif flag == 1:
            if w == 0:
                flag = 0
                count = 0
            if w == 1:
                count += 1
        if count >= 6:
            print("#coderlifematters")
            flag2 = 1
            break
    if flag2 == 0:
        print("#allcodersarefun")
