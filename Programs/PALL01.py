for i in range(int(input())):
    n = int(input())
    a = n
    rev = 0
    while a != 0:
        rev = rev*10 + a%10
        a //= 10
    if rev == n:
        print("wins")
    else:
        print("losses")
