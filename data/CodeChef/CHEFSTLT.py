for i in range(int(input())):
    str1 = input()
    str2 = input()
    mindiff = maxdiff = 0
    for a, b in zip(str1, str2):
        if a != '?' and b != '?' and a!=b:
            mindiff += 1
            maxdiff += 1
        elif a == '?' or b == '?':
            maxdiff += 1
    print(str(mindiff)+" "+str(maxdiff))
