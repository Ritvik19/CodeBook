for t in range(int(input())):
    up = input()
    down = input()
    flag = 'no'
    for i in range(3):
        if up[i] == 'o' or down[i] == 'o':
            count = 0
            for j in range(3):
                if j != i:
                    if up[j] == 'b' or down[j] == 'b':
                        count += 1
                if count == 2:
                    flag = 'yes'
    print(flag)
