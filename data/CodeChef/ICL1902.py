for t in range(int(input())):
    n = int(input())
    count = 0
    while n != 0:
        count += 1
        n -= int(n**0.5)**2
    print(count)
