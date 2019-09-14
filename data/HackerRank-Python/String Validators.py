if __name__ == '__main__':
    string = list(input())
    flag = False
    for s in string:
        if s.isalnum():
            flag = True
            break
    print(flag)

    flag = False
    for s in string:
        if s.isalpha():
            flag = True
            break
    print(flag)

    flag = False
    for s in string:
        if s.isdigit():
            flag = True
            break
    print(flag)

    flag = False
    for s in string:
        if s.islower():
            flag = True
            break
    print(flag)

    flag = False
    for s in string:
        if s.isupper():
            flag = True
            break
    print(flag)
