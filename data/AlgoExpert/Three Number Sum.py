def threeNumberSum(array, targetSum):
    results = []
    array = sorted(array)
    for i in range(len(array) - 2):
        a = array[i]
        left = i + 1
        right = len(array) - 1
        while left < right:
            b = array[left]
            c = array[right]
            if a + b + c < targetSum:
                left += 1
            elif a + b + c > targetSum:
                right -= 1
            else:
                results.append([a, b, c])
                left += 1
                right -= 1
    return results