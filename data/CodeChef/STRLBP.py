def STRLBP(x):
    trans = 0
    if x[0] != x[7]:
        trans = 1
    i=0
    while i<7 and trans <= 2:
        if x[i] != x[i+1]:
            trans += 1
        i+=1
    return trans

def uni(x):
    if x <= 2:
        return "uniform"
    else:
        return "non-uniform"

a = []
t = int(input())
for i in range(t):
    a.append(input())
for i in range(t):
        print(uni(STRLBP(a[i])))
