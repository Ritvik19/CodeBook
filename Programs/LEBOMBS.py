for t in range(int(input())):
    n = int(input())
    S = input()
    a = [0]*n
    for i in range(n):
        if S[i] == '1':
            if i == 0:
                a[i] = 1
                if i < n-1:
                    a[i+1] = 1
            elif i == n-1:
                a[i] = 1
                if i > 0:
                    a[i-1] = 1
            else:
                a[i] = 1
                a[i-1] = 1
                a[i+1] = 1
    print(a.count(0))
