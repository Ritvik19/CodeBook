for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split(' ')))
    i = 0
    out = []

    while (i<n): 
        begin = i
        if (i == n-1):
            end = i
        else:
            while (a[i+1] == a[i]+1):
                i = i+1
                if (i == n-1):
                    break
        end = i

        if (begin == end):
            out.append(a[begin])
        
        elif (begin + 1 == end):
            out.append(a[begin])
            out.append(a[end])
        else:
            out.append("{}...{}".format(a[begin],a[end]))
        
        i = i+1
    listToStr = ",".join(str(x) for x in out)
    print(listToStr)