for t in range(int(input())):
    n = int(input())
    ans = ["", "", ""]
    if 360%n == 0:
        ans[0] = "y"
    else:
        ans[0] = "n"
    if n<=360:
        ans[1] = "y"
    else:
        ans[1] = "n"
    if n*(n+1)//2<= 360:
        ans[2] = "y"
    else:
        ans[2] = "n"
    print(*ans)
