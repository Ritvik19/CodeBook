def newres(res, arr, MOD):
    arrsq = [elt*elt%MOD for elt in arr]
    return set((a+b)%MOD for a in arrsq for b in res)

k, m = map(int, input().split())
res = {0}
for i in range(k):
    n, *L = list(map(int, input().split()))
    res = newres(res, L, m)
print(max(res))
