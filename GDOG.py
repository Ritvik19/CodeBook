for i in range(int(input())):
    n,k = input().split()
    n,k = int(n),int(k)
    max = 0
    for i in range(1,k+1):
        if n%i>max:
            max = n%i
    print(max)
