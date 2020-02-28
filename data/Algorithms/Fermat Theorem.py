from random import randint


def power(a, n, p):
    """
    a ** n % p
    """
    res = 1
    a = a % p

    while n > 0:
        if n & 1:
            res = (res*a) % p
        n = n >> 1
        a = (a*a) % p
    return res


def gcd(a, b):
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b
    else:
        return gcd(b, a % b)


def isPrime(n, k):
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True

    while k > 0:
        a = 2 + randint(2, n-1) % (n-4)

        if gcd(n, a) != 1:
            return False

        if power(a, n-1, n) != 1:
            return False

        k -= 1

    return True


if __name__ == '__main__':
    print(isPrime(11, 3))
    print(isPrime(15, 3))
