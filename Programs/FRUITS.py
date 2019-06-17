for i in range(int(input())):
    inp = input().split(" ")
    n = int(inp[0])
    m = int(inp[1])
    k = int(inp[2])

    if k <= abs(n-m):
        print(abs(n-m)-k)
    # elif (k-abs(n-m))%2 != 0:
        # print(1)
    else:
        print(0)
