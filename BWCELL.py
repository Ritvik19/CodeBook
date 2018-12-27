for t in range(int(input())):
    S = input().strip()
    n = len(S)
    w = S.index('W')
    if n%2 == 1 and w == n//2 :
        print('Chef')
    else:
        print('Aleksa')
