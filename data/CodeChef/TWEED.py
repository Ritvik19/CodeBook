for t in range(int(input())):
    x,p = input().split()
    n = int(x)
    A = [int(i) for i in input().split()]
    if n==1 and A[0]%2==0 and p == "Dee":
        print("Dee")
    else:
        print("Dum")
