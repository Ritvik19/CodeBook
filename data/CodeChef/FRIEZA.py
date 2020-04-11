for t in range(int(input())):
    good = ['f', 'r', 'i', 'e', 'z', 'a']
    string = input()
    gcount = 0
    bcount = 0
    code = ""
    for s in string:
        if s in good:
            gcount += 1
            if bcount != 0:
                code += str(bcount)
            bcount = 0
        else:
            bcount += 1
            if gcount != 0:
                code += str(gcount)
            gcount = 0
    if gcount:
        code += str(gcount)
    if bcount:
        code += str(bcount)
    print(code)
