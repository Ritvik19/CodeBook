for t in range(int(input())):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    count = 0
    for nm in nums:
        if (nm + k)%7 == 0:
            count += 1
    print(count)
