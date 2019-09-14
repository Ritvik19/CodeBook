for t in range(int(input())):
    S = input()
    sum = 0
    for s in S:
        if "0" <= s <= "9":
            sum += int(s)
    print(sum)
