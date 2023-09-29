def missingNumbers(nums):
    included = set(nums)

    missing = []
    for num in range(1, len(nums) + 3):
        if num not in included:
            missing.append(num)

    return missing
