for i in range(int(input())):
    inp = input().split(" ")
    n = int(inp[0])
    b = int(inp[1])
    m = int(inp[2])
    t = 0
    a = n
    op = 0
    while n != 0:
        op += ((n+1)//2)*m*(2**t)
        n -= (n+1)//2
        t += 1
    op += (t-1)*b
    print(op)
