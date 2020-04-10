for _ in range(int(input())):
    n = int(input())
    lost = 0
    for _ in range(n):
        price, quantity, discount = map(int, input().split())
        percent1 = 1 + discount / 100
        percent2 = (100 - discount) / 100

        originalTot = price * quantity
        tot = price * percent1 * percent2 * quantity
        lost += originalTot - tot

    print(f'{lost:.9f}')