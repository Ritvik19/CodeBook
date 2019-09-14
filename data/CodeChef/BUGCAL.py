for i in range(int(input())):
    inp=input()
    a=int(inp.split(" ")[0])
    b=int(inp.split(" ")[1])
    sum = ""
    while(a!=0 or b!=0):
        sum=str((a%10+b%10)%10) + sum
        a=int(a/10)
        b=int(b/10)
    print (int(sum))
