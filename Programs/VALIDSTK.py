for t in range(int(input())):
    n = int(input())
    instructions = list(map(int, input().split()))
    num = 0
    out = 'Valid'
    for i in instructions:
        if i == 1:
            num += 1
        if i == 0:
            if num == 0:
                out = 'Invalid'
                break
            num -= 1
    print(out)
