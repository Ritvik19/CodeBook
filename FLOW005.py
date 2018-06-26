for i in range(int(input())):
    n = int(input())
    num = 0

    num += n//100
    n %= 100

    num += n//50
    n %= 50

    num += n//10
    n %= 10

    num += n//5
    n %= 5

    num += n//2
    n %= 2

    num += n

    print(num)
