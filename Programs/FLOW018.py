def fact(n):
    f =1
    for i in range(1,n+1):
        f *= i
    return f

for i in range(int(input())):
    print(fact(int(input())))
