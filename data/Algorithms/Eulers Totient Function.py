def phi(n):
    result = n
    p = 2
    while(p * p <= n):
        if (n % p == 0):
            while (n % p == 0):
                n = n // p
            result = result * (1.0 - (1.0 / (float)(p)))
        p = p + 1

    if (n > 1):
        result = result * (1.0 - (1.0 / (float)(n)))

    return (int)(result)


if __name__ == '__main__':
    for n in range(1, 16):
        print("phi(", n, ") = ", phi(n))
