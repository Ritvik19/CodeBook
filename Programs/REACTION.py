for t in range(int(input())):
    n, m = map(int, input().split())
    flag = 'Stable'
    for i in range(n):
        row = list(map(int, input().split()))
        if i == 0 or i == n-1:
            if row[0] > 1 or row[-1] > 1:
                flag = 'Unstable'
            if max(row[1:-1]) > 2:
                flag = 'Unstable'
        else:
            if row[0] > 2 or row[-1] > 2:
                flag = 'Unstable'
            if max(row[1:-1]) > 3:
                flag = 'Unstable'
    print(flag)
