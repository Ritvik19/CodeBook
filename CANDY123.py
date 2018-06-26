for i in range(int(input())):
    a, b = input().split()
    a, b = int(a), int(b)
    i = 0
    while a>=0 and b>=0:
        i += 1
        if i%2 == 1:
            a -= i
        else:
            b -= i
        if a<0:
            print("Bob")
        elif b<0:
            print("Limak")
