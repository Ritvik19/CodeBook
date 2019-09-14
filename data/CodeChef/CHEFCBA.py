nums = list(map(int, input().split()))
nums = list(sorted(nums))
if nums[0] * nums[3] == nums[1] * nums[2]:
    print("Possible")
else:
    print("Impossible")
