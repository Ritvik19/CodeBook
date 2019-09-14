for i in range(int(input())):
    n, k = input().split()
    n, k = int(n), int(k)
    arr = [int(e) for e in input().split()]
    if k > 1:
        print("even")
    else:
        sum = 0
        for e in arr:
            sum += e
        if sum %2 == 0:
            print("odd")
        else:
            print("even")
