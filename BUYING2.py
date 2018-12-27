for t in range(int(input())):
    n, x = map(int, input().split())
    notes = [int(e) for e in input().split()]
    sweets = sum(notes)//x
    if (sum(notes)-min(notes)) < sweets:
        print(-1)
    else:
        print(sweets)
