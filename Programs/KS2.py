for t in range(int(input())):
    n = input()
    for i in range(10):
        b = n+str(i)
        if sum([ int(x) for x in b ]) % 10 == 0:
            print(b)
            break
