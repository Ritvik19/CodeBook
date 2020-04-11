for t in range(int(input())):
    a, b, c = map(int, input().split())
    # count = 0
    # if (a + c) %2 != 0:
    #      if a > c:
    #          a -= 1
    #          count += 1
    #      else:
    #         a += 1
    #         count += 1
    # count += abs(b-((a+c)//2))
    # print(count)
    if (a+c)%2 == 0:
        print(abs((a+c)//2-b))
    else:
        if a+c>2*b:
            print(abs((a+c)//2-b+1))
        else:
            print(abs((a+c)//2-b))
