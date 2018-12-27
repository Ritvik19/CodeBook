for t in range(int(input())):
    k = int(input())
    c = "a"
    w = ""
    for i in range(k + (k-1)//25+1):
        w = chr(ord(c)+(i%26)) + w
    print(w)
