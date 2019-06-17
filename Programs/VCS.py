for i in range(int(input())):
    n, m, k = input().split()
    n, m, k = int(n), int(m), int(k)
    a = [int(e) for e in input().split()]
    b = [int(e) for e in input().split()]

    ti = utui  = 0
    for j in range(1, n+1):
        if j in a and j in b:
            ti += 1
        elif j not in a and j not in b:
            utui += 1
    print(str(ti)+" "+str(utui))
