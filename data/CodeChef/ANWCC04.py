for t in range(int(input())):
    s = input()
    l, r = s.split('=')
    r = int(r)
    beg = 0
    a = []
    for i in range(len(l)):
        if l[i] == '+' or l[i] == '-':
            a.append(int(l[beg:i]))
            a.append(l[i])
            beg = i+1
            if len(a) == 4:
                a.append(int(l[beg:]))
                break
    res = a[0]
    for i in range(1,5,2):
        if a[i] == '+':
            res += a[i+1]
        else:
            res -= a[i+1]
    print('Invalid  Equation' if res != r else 'Valid  Equation')
