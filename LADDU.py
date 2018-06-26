for t in range(int(input())):
    a , o = input().split()
    laddu = 0
    for i in range(int(a)):
        act = input().split()
        if act[0] == "CONTEST_WON":
            if int(act[1]) < 20:
                laddu += 20 - int(act[1])
            laddu += 300
        if act[0] == "TOP_CONTRIBUTOR":
            laddu += 300
        if act[0] == "CONTEST_HOSTED":
            laddu += 50
        if act[0] == "BUG_FOUND":
            laddu += int(act[1])
    if o == "INDIAN":
        print(laddu//200)
    else:
        print(laddu//400)
