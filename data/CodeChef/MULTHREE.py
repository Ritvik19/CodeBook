"""
    d0 = (d0)
    d1 = (d1)
    d2 = (d0 + d1)
    d3 = d0 + d1 + d2 = 2 (d0 + d1)
    d4 = d0 + d1 + d2 + d3 = 4 * (d0 + d1)
    d5 = d0 + d1 + d2 + d3  + d4 = 4 * (d0 + d1) + 2 * (d0 + d1) + (d0 + d1) + d0 + d1 = 8 (d0 + d1)
    d6 = ( d0 + d1 ) * (8 + 4 + 2 + 1 + 1) = 6 * (d0 + d1)
    d7 = 2 * (d0 + d1)
"""
for t in range(int(input())):
    k,d0,d1=map(int,input().split())
    d2=(d0+d1)%10
    d3=(d2*2)%10
    d4=(d3*2)%10
    d5=(d4*2)%10
    d6=(d5*2)%10
    l=[d3,d4,d5,d6]
    if k==2:
        if(d0+d1)%3==0:
            print("YES")
        else:
            print("NO")
    elif k==3:
        if (d0+d1+d2)%3==0:
            print("YES")
        else:
            print("NO")
    else:
        sm=(d0+d1+d2)+(d3+d4+d5+d6)*((k-3)//4)
        sm+=sum(l[:(k-3)%4])
        if sm%3==0:
            print("YES")
        else:
            print("NO")
            