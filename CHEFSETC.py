for t in range(int(input())):
    set = list(map(int, input().split()))
    flag = 0
    for i in range(16):
        subset = []
        for j in range(4):
            if i & 1 << j:
                subset.append(set[j])
        if len(subset) > 0 and sum(subset) == 0:
            flag = 1
            break
    if flag == 1:
        print("Yes")
    else:
        print("No")
