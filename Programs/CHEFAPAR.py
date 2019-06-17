for t in range(int(input())):
    n = int(input())
    dues = n*1100
    pay = [int(e) for e in input().split()]
    flag = 0
    for i in pay:
        if flag == 0 and i == 1:
            dues -= 1100
        if flag == 1 and i == 1:
            dues -= 1000
        if i == 0:
            flag = 1
    print(dues)
