for t in range(int(input())):
    s = list(input())
    for i in range(len(s)):
        if s[i] == "m":
            if i != 0 and s[i-1] == "s":
                s[i-1] = ""
            elif i != len(s)-1 and s[i+1] == "s":
                s[i+1] = ""

    snakesLeft = s.count("s")
    mongoosesLeft = s.count("m")

    if snakesLeft > mongoosesLeft:
        print("snakes")
    elif snakesLeft < mongoosesLeft:
        print("mongooses")
    else:
        print("tie")
