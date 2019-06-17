for t in range(int(input())):
    ques = input()
    flag = 0
    for i in range(26):
        if chr(65+i) not in ques and chr(97+i) not in ques:
            print(chr(65+i)+chr(97+i))
            flag = 1
            break
    if flag == 0:
        print("~")
