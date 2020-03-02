def power(x, y):
    if(y == 0):
        return 1
    temp = power(x, int(y / 2))

    if (y % 2 == 0):
        return temp * temp
    else:
        if(y > 0):
            return x * temp * temp
        else:
            return (temp * temp) / x


if __name__ == '__main__':
    x, y = 2, -3
    print(f"{power(x, y):.6f}")
