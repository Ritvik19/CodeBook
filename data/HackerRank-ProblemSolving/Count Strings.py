MOD = 10 ** 9 + 7
def mod(x): return (x % MOD)

AND, OR, KLEEN = None, False, True
A, B, E = True, False, None

def generateId():
    x = 0
    while True:
        yield x
        x += 1

def parse(s):
    t, op = [()], []
    for i in s:
        if i == '(':
            t.append(())
            op.append(AND)
        elif i == ')':
            x = ((op.pop(), t.pop()), )
            t[-1] += x
        elif i == 'a':
            t[-1] += (A,)
        elif i == 'b':
            t[-1] += (B,)
        elif i == '|':
            op[-1] = OR
        elif i == '*':
            op[-1] = KLEEN
    return t.pop()[0]

def nfa(t, g=None):
    global ID
    if g is None:
        g = {}
    if isinstance(t, tuple):
        g, a, b = nfa(t[1][0], g)
        if t[0] == KLEEN:
            x, y = next(ID), next(ID)
            g[x] = {E: {a, y}}
            g.setdefault(b, {}).setdefault(E, set()).update({a, y})
            return g, x, y
        else:
            g, x, y = nfa(t[1][1], g)
            if t[0] == AND:
                g.setdefault(b, {}).setdefault(E, set()).add(x)
                return g, a, y
            p, q = next(ID), next(ID)
            g[p] = {E: {a, x}}
            g.setdefault(b, {}).setdefault(E, set()).add(q)
            g.setdefault(y, {}).setdefault(E, set()).add(q)
            return g, p, q
    else:
        x, y = next(ID), next(ID)
        g[x] = {t: {y}}
        return g, x, y

def eps(x, n):
    d, v = set(), x
    while v:
        x = v.pop()
        if x not in d:
            d.add(x)
            v.update(n.get(x, {}).get(E, set()))
    return d

def setuple(x):
    return tuple(sorted(x))

def dfa(n, s, e):
    ID = generateId()
    f, d, v, g = {}, {}, set(), set()
    s = eps({s}, n)
    x = next(ID)
    if e in s:
        g.add(x)
    s = setuple(s)
    v.add(s)
    f[s] = x
    while v:
        s = v.pop()
        if f[s] not in d:
            d[f[s]] = []
            for i in (A, B):
                z = set()
                for j in s:
                    z.update(n.get(j, {}).get(i, set()))
                y = eps(z, n)
                z = setuple(y)
                if z not in f:
                    x = next(ID)
                    v.add(z)
                x = f.setdefault(z, x)
                if e in y:
                    g.add(x)
                d[f[s]].append(x)
    return d, g

def mat(x):
    y = len(x)
    return list(map(lambda i: list(map(x[i].count, range(y))), range(y)))

def identity(n):
    return list(map(lambda i: list(map(lambda j: int(i == j), range(n))), range(n)))

def multiply(a, b):
    n = len(a)
    return list(map(lambda i: list(map(lambda j: mod(sum(map(lambda k: mod(a[i][k] * b[k][j]), range(n)))), range(n))), range(n)))

def modpow(x, n):
    y = identity(len(x))
    while n:
        if n & 1:
            y = multiply(x, y)
        x = multiply(x, x)
        n >>= 1
    return y

def valid_sum(a, g):
    return mod(sum(map(a.__getitem__, g)))

def solve(s, l):
    d, g = dfa(*nfa(parse(s)))
    return valid_sum(modpow(mat(d), l)[0], g)

for _ in range(int(input())):
    ID = generateId()
    s, l = input().split()
    if s == 'a' or s == 'b':
        print(1 if l == '1' else 0)
    else:
        print(solve(s, int(l)))
