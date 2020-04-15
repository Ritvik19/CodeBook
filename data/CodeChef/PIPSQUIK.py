for _ in range(int(input())):
    n, h, y1, y2, l = map(int,input().split())
    count = 0
    
    for i in range(n):
        a = list(map(int, input().split()))
        if l > 0 :
            if a[0] == 1:
                if (h - y1) <= a[1]:
                    count += 1
                else:
                    l -= 1
                    if l>0:
                        count += 1
            elif a[0] == 2:
                if y2 >= a[1]:
                    count += 1
                else:
                    l -= 1
                    if l > 0:
                        count += 1
            else:
                break
    print(count)