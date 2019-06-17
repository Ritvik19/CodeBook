for t in range(int(input())):
    n = int(input())
    seq = []
    k = 2*3*5*7*11
    a = n//3
    if n%3 == 0:
        for i in range(a):
            seq.append(k*i+6)
            seq.append(k*i+10)
            seq.append(k*i+15)
    elif n%3 == 1:
        for i in range(a-1):
            seq.append(k*i+6)
            seq.append(k*i+10)
            seq.append(k*i+15)
        seq.append(k*a+6)
        seq.append(k*a+10)
        seq.append(k*a+35)
        seq.append(k*(a+1)+21)
    else:
        for i in range(a-1):
            seq.append(k*i+6)
            seq.append(k*i+10)
            seq.append(k*i+15)
        seq.append(k*a+6)
        seq.append(k*a+10)
        seq.append(k*a+55)
        seq.append(k*(a+1)+77)
        seq.append(k*(a+1)+21)
    print(*seq)
