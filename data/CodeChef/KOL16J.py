for i in range(int(input())):
    n = int(input())
    chap = [int(e) for e in input().split()]
    if chap == sorted(chap) or max(chap) > n or sorted(chap) != list(set(chap)):
        print("no")
    else:
        print("yes")
