for t in range(int(input())):
    price = list(map(int, input().split()))
    cost = 0
    pangram = input()
    for alph, i in zip("abcdefghijklmnopqrstuvwxyz", range(26)):
        if alph not in pangram:
            cost += price[i]
    print(cost)
