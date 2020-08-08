for t in range(int(input())):
    S = input()
    n = len(S)
    if n <=2:
        print("YES")
    else:
        l = S[1:] + S[:1]
        r = S[n-1:] + S[:n-1]
        
        print("YES") if l == r else print("NO")