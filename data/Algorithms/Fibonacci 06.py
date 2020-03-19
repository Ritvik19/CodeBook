MAX = 1000

f = [0] * MAX


def fibonacci(n):
    if (n == 0):
        return 0
    if (n == 1 or n == 2):
        f[n] = 1
        return (f[n])

    if (f[n]):
        return f[n]

    if(n & 1):
        k = (n + 1) // 2
    else:
        k = n // 2

    if((n & 1)):
        f[n] = (fibonacci(k) * fibonacci(k) + fibonacci(k-1) * fibonacci(k-1))
    else:
        f[n] = (2*fibonacci(k-1) + fibonacci(k))*fibonacci(k)

    return f[n]


if __name__ == "__main__":
    print("""If n is even then k = n/2:
F(n) = [2*F(k-1) + F(k)]*F(k)

If n is odd then k = (n + 1)/2
F(n) = F(k)*F(k) + F(k-1)*F(k-1)""")
    print(fibonacci(9))
