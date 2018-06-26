for t in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    sums = []
    for i in range(n):
        for j in range(i+1, n):
            sums.append(nums[i]+nums[j])
    count = 0
    for sum in sums:
        if sum == max(sums):
            count += 1
    print("{:0.8f}".format(count/len(sums)))
