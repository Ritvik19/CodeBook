def missing(dolls):
    for i in range(len(dolls)//2):
        if dolls[2*i] != dolls[2*i+1]:
            return dolls[2*i]
    return dolls[len(dolls)-1]
for i in range(int(input())):
    a = []
    n = int(input())
    for j in range(n):
        a.append(int(input()))
    print(missing(sorted(a)))
