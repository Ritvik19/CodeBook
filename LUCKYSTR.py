def func(good, s):
    for g in good:
        if g in s:
            return True
    return False

k, n = map(int, input().split())
good = []
lucky = []

for i in range(k):
    good.append(input())

for i in range(n):
    s = input()
    if len(s) >= 47:
        print("Good")
    else:
        if func(good, s):
            print("Good")
        else:
            print("Bad")
