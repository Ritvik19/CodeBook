for i in range(int(input())):
    s = []
    n = int(input())
    for j in range(n):
        s.append(input())
    if n < 5 :
        print("No")
    else:
        if "cakewalk" in s and "simple" in s and "easy" in s and ("easy-medium" in s or "medium" in s) and ("medium-hard" in s or "hard" in s):
            print("Yes")
        else:
            print("No")
