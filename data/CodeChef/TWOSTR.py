for i in range(int(input())):
    str1 = input()
    str2 = input()
    diff = 0
    for a, b in zip(str1, str2):
        if a != '?' and b != '?' and a!=b:
            diff += 1
    if diff != 0:
        print("No")
    else:
        print("Yes")
