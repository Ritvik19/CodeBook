def gcd(a, b):
    if a == 0:
        return b

    return gcd(b % a, a)


if __name__ == '__main__':
    a = 10
    b = 15
    print("GCD(", a, ",", b, ") = ", gcd(a, b))

    a = 35
    b = 10
    print("GCD(", a, ",", b, ") = ", gcd(a, b))

    a = 31
    b = 2
    print("GCD(", a, ",", b, ") = ", gcd(a, b))
