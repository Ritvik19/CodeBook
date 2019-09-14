for i in range(int(input())):
    inp = input()
    n = int(inp.split(" ")[0])
    k = int(inp.split(" ")[1])
    s = input()
    sm = 0
    cp = 0
    for ch in s:
        if ord(ch) in range(65, 91):
            cp += 1
        elif ord(ch) in range(97, 123):
            sm += 1
    if sm <= k and cp <= k:
        print("both")
    else:
        if sm <= k:
            print("brother")
        elif cp <= k:
            print("chef")
        else:
            print("none")
