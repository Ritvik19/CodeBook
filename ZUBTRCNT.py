for t  in range(int(input())):
    l, k = map(int, input().split())
    x = l - k + 1
    if k > l:
        print("Case {}: {}".format(t+1,0))
    else:
        print("Case {}: {}".format(t+1,x*(x+1)//2))
