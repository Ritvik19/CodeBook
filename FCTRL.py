def zeros(n):
    if n<5:
        return 0
    elif (n>=5 and n<10):
        return 1
    else:
        return (n//5+zeros(n//5))

for i in range(int(input())):
    print(zeros(int(input())))
