def mirror(x):
    return chr(97+26-ord(x)+96)

for t in range(int(input())):
    n = int(input())
    s = list(input())
    for i in range(n):
        s[i] = mirror(s[i])
    if n%2 == 1:
        n-=1
    i = 0
    while i < n:
        s[i], s[i+1] = s[i+1], s[i]
        i += 2
    print(''.join(s))
