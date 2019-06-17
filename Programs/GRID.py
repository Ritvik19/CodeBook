for t in range(int(input())):
    n = int(input())
    count = 0
    for i in range(n):
        row = input()
        row = reversed(row)
        for r in row:
            if r == ".":
                count += 1
            else:
                break
    print(count)
