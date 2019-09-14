for i in range(int(input())):
    n, k = input().split(" ")
    A = [int(i) for i in input().split(" ")]
    B = sorted(A)
    print(B[(int(n)+int(k))//2])
