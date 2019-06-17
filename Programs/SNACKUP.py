for t in range(int(input())):
    n = int(input())
    print(n)
    a=[(i%n)+1 for i in range(n)]
    for i in range(n):
        print(n)
        k=i
        for j in range(n):
            print(j+1, a[k%n], a[(k+1)%n])
            k += 1
