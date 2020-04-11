for t in range(int(input())):
    s = input()
    op = ""
    for c in s:
        if ord(c) in range(97, 123):
            op += chr(219-ord(c))
        elif ord(c) in range(65, 91):
            op += chr(155-ord(c))
        else:
            op += c
    print(op)
