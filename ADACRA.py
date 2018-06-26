for i in range(int(input())):
    s = input()
    chng = 0
    for i in range(1,len(s)):
        if s[i] != s[i-1]:
            chng += 1
    print((chng+1)//2)
