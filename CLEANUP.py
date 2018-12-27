for t in range(int(input())):
    n, m = map(int, input().split())
    done = [int(e) for e in input().split()]
    chef = []
    astnt = []
    count = 0
    for i in range(1, n+1):
        if i not in done:
            count += 1
            if count %2 == 0:
                astnt.append(i)
            else:
                chef.append(i)
    print(*chef)
    print(*astnt)
