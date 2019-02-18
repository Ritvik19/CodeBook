for t in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    A.sort()
    attended = 0
    for a in A:
        if attended >= a:
            attended += 1
        else:
            break
    print(attended)
