def squareRoot(n):
        x = n
        y = 1

        e = 0.000001
        while(x - y > e):
            x = (x + y)/2
            y = n / x

        return x


if __name__ == '__main__':
    n = 2
    print("Square root of", n, "is", squareRoot(n))
