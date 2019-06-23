for t in range(int(input())):
    n = int(input())
    names = []
    for i in range(n):
        names.append(input().split())
    fname_count = dict()
    for n in names:
        if n[0] not in fname_count.keys():
            fname_count[n[0]] = 0
        fname_count[n[0]] += 1
    for n in names:
        if fname_count[n[0]] == 1:
            print(n[0])
        else:
            print(' '.join(n))
