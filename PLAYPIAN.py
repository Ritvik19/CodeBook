for t in range(int(input())):
    s = input()
    i = 0
    flag = 0
    while i < len(s):
        if s[i] == s[i+1]:
            flag = 1
            break
        i += 2
    if flag == 1:
        print('no')
    else:
        print('yes')
