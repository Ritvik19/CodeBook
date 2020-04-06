n = int(input())
brackets = list(map(int, input().split()))
s = []
c = 0
iDe = 0
de = 0
iBet = 0
bet = 0

for i in range(n):
    c += 1
    if brackets[i] == 1:
        s.append(brackets[i])
    else:
        if len(s) > de:
            iDe = i
            de = len(s)
        s.pop(-1)
        if len(s) == 0:
            if c > bet:
                bet = c
                iBet = i - bet
            c = 0

print(de, iDe, bet, iBet+2)