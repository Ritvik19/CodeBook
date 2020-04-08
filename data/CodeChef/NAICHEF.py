for i in range(int(input())):
    n,x,y=map(int,input().split())
    l=list(map(int,input().split()))
    w,z=l.count(x),l.count(y)
    print((w/n)*(z/n))