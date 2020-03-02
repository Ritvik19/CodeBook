def SieveOfEratosthenes(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1

    ret = []
    for p in range(2, n):
        if prime[p]:
            ret.append(p)

    return ret


if __name__ == '__main__':
    n = 30
    print("Following are the prime numbers smaller than or equal to", n)
    print(*SieveOfEratosthenes(n))
