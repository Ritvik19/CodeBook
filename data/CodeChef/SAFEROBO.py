for t in range(int(input())):
    S = input()
    sa, sb = map(int, input().split())
    a = S.index('A')
    b = S.index('B')
    flag = 1
    while a < len(S) and b >= 0 and a < b:
        a = a + sa
        b = b - sb
        
        if a == b:
            print('unsafe')
            flag = 2
            break
    if flag == 1:
        print('safe')