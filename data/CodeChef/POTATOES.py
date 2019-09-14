def isprime(num):
    for i in range(2, num//2+1):
        if num % i == 0:
            return False
    return True
for t in range(int(input())):
    x, y = map(int, input().split())
    i = 1
    while True:
        if isprime(x+y+i):
            print(i)
            break
        i += 1
