for t in range(int(input())):
    s = input()

    tot = 0
    for i in range(len(s) - 3):
        S = set(list(s[i:i+4]))

        if S == {'c', 'h', 'e', 'f'}:
            tot += 1

    if tot:
        print(f'lovely {tot}')
    else:
        print('normal')
