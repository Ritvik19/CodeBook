for t in range(int(input())):
    a, b, c, x, y, z = map(int, input().split())
    d=[(a,x), (b,y), (c,z)]
    
    d.sort()
    count=0
    for i in range(2):
        if d[i][0] == d[i+1][0]:
            if d[i][1] == d[i+1][1]:
                pass
            else:
                count = 1
        else:
            if d[i][1] < d[i+1][1]:
                pass
            else:
                count = 1
        if count == 1:
            break
    if count == 0:
        print('FAIR')
    else:
        print('NOT FAIR') 