for t in range(int(input())):
    s = input()
    n = len(s)
    n1 = list(s[:n//2])
    if n %2 == 0:
        n2 = list(s[n//2:])
    else:
        n2 = list(s[n//2+1:])
    if sorted(n1) == sorted(n2):
        print("YES")
    else:
        print("NO")
