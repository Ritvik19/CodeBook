def sum(d, n):
    if d == 1:
        return n*(n+1)//2
    else:
        return sum(1,sum(d-1, n))

for i in range(int(input())):
    d, n = input().split(" ")
    print(sum(int(d), int(n)))
