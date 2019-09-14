for i in range(int(input())):
    a = input().split()
    b = input().split()
    same = 0
    for ing in a:
        if ing in b:
            same += 1
    if same >= len(a)//2:
        print("similar")
    else:
        print("dissimilar")
