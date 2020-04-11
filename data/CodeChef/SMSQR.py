for t in range(int(input())):
    x, y = map(int, input().split())
    sum = y*(2*y+1)*(2*y-1)//3 - x*(2*x+1)*(2*x-1)//3
    print(sum%1000000007)
