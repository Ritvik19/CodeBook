for i in range(int(input())):
    inp = input().split(" ")
    n = int(inp[0])
    p = int(inp[1])
    l = [int(e) for e in input().split(" ")]
    cw = 0
    df = 0
    for e in l:
        if e >= p//2:
            cw += 1
        elif e <= p//10:
            df += 1
    if cw == 1 and df == 2:
        print("yes")
    else:
        print("no") 
