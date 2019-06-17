C = H = E = F = 0
S = input()
for s in S:
    if s == 'C':
        C += 1
    elif s == "H" and C > H:
        H += 1
    elif s == "E" and H>E:
        E += 1
    elif s == "F" and E>F:
        F += 1
print(F)
