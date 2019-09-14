for t in range(int(input())):
    logo = []
    for i in range(3):
        logo.append(input())
    flag = 'no'
    for i in range(2):
        for j in range(2):
            if logo[i][j] == 'l' and logo[i+1][j] == 'l' and logo[i+1][j+1] == 'l':
                flag = 'yes'
                break
    print(flag)
