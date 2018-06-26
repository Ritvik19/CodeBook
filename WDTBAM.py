for i in range(int(input())):
    n = int(input())
    crct = input()
    chef = input()
    W = [int(e) for e in input().split(" ")]
    x = 0
    for a, b in zip(crct, chef):
        if a == b:
            x += 1
    if x == n:
        print(W[-1])
    else:
        print(max(W[:x+1]))
