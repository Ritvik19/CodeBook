def isprime(n):
    if n == 1:
        return False
    if n != 2 and n%2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n%i == 0:
            return False
    return True

n,m = map(int, input().split())
primes = 0
for i in range(2, n+m+1):
    primes += int(isprime(i))
print(primes)
