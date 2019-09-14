def mxbal(arr):
    mxbl = 0
    bl = 0
    for a in arr:
        if a == '(':
            bl += 1
        else:
            bl -= 1
        mxbl = max(mxbl, bl)
    return "("*mxbl + ")"*mxbl


for t in range(int(input())):
    print(mxbal(input()))
