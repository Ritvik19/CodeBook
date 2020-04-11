for t in range(int(input())):
    string = input()
    flag = 0
    for ch in ["a", "e", "i", "o", "u"]:
        if ch not in string:
            flag = 1
            break
    if flag == 0:
        print(string)
