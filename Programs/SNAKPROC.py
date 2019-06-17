for i in range(int(input())):
    n = int(input())
    snake = input()
    flag = 0
    i = 0
    while i < n and flag >=0 and flag < 2  :
        if snake[i] == "H":
            flag += 1
        elif snake[i] == "T":
            flag -= 1
        i += 1
    if flag == 0:
        print("Valid")
    else:
        print("Invalid")
