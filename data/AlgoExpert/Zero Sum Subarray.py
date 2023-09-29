def zeroSumSubarray(nums):
    sums = set([0])
    current_sum = 0
    for num in nums:
        current_sum += num
        if current_sum in sums:
            return True
        sums.add(current_sum)
    return False
