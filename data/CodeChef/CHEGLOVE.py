for _ in range(int(input())):
    n = int(input())
    finger = list(map(int, input().split()))
    glove = list(map(int, input().split()))
    front = []
    back = []
    for i in range(n):
        if glove[i] >= finger[i]:
            front.append(1)
        else:
            front.append(0)
        if glove[n-1-i] >= finger[i]:
            back.append(1)
        else:
            back.append(0)
    if all(front) and all(back):
        print("both")
    elif all(front):
        print("front")
    elif all(back):
        print("back")
    else:
        print("none")