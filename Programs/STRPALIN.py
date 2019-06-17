for t in range(int(input())):
    A = input()
    B = input()
    flag = 0
    for i in A:
        for j in B:
            if i == j:
                flag = 1
                break
        if flag == 1:
            break
    if flag == 1:
        print("Yes")
    else:
        print("No")        
