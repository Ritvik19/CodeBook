pct = float(input())
pot = float(input())
N = int(input())

print("{:.6f}".format(round(pot*(1-pct) + pct*2/N, 6)))
