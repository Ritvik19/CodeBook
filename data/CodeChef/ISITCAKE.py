for t in range(int(input())):
    count = 0
    for i in range(10):
        A = list(map(int, input().split()))
        for a in A:
            if a <= 30:
                count += 1
    if count >= 60:
        print('yes')
    else:
        print('no')