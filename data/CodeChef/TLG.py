mxm , wnr, x, y = 0
for i in range(input()):
    s, t = input().split(" ")
    x += int(s)
    y += int(t)
    if abs(x-y) > mxm:
        mxm = abs(x-y)
        if x > y:
            wnr = 1
        else:
            wnr = 2
print(str(wnr)+" "+str(mxm))
