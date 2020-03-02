def stockBuySell(price):
    n = len(price)
    if (n == 1):
        return

    i = 0
    while (i < (n - 1)):

        while ((i < (n - 1)) and
                (price[i + 1] <= price[i])):
            i += 1

        if (i == n - 1):
            break

        buy = i
        i += 1

        while ((i < n) and (price[i] >= price[i - 1])):
            i += 1

        sell = i - 1

        print("Buy on day: ", buy, "\tSell on day: ", sell)


if __name__ == '__main__':
    price = [100, 180, 260, 310, 40, 535, 695]
    stockBuySell(price)
