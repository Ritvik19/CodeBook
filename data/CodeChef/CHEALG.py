for t in range(int(input())):
    s=input()
    ans=""
    c=1
    
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            c += 1 
        else:
            ans += s[i] + str(c)
            c = 1
            
    ans += s[len(s) - 1] + str(c)
    
    if len(ans) < len(s):
        print("YES")
    else:
        print("NO")