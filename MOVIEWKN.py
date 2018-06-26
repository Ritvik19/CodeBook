for i in range(int(input())):
    n = int(input())
    L = [int(e) for e in input().split(" ")]
    R = [int(e) for e in input().split(" ")]
    LR = []
    for l, r in zip(L, R):
        LR.append(l*r)
    chLR = chR = chi = 0
    for i in range(len(LR)):
        if LR[i] > chLR:
            chLR = LR[i]
            chR = R[i]
            chi = i
        elif LR[i] == chLR and R[i] > chR:
             chLR = LR[i]
             chR = R[i]
             chi = i
    print(chi +1)
