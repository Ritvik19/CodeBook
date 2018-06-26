for i in range(int(input())):
    s = input()
    if '1' not in s:
        print("NO")
    else:
        chng = 0
        i = 1
        while i<len(s) and chng <= 2:
            if s[i] != s[i-1]:
                chng += 1
            i+=1
        if chng == 2 and s[0] == '0':
            print("YES")
        elif chng <= 1:
            print("YES")
        else:
            print("NO")
