# O(n) O(n)

def twoNumberSum(array, targetSum):
    hashmap = {}
    for num in array:
        if targetSum - num in hashmap:
            return [num, targetSum - num]
        else:
            hashmap[num] = True
    return []

twoNumberSum(**{
  "array": [3, 5, -4, 8, 11, 1, -1, 6],
  "targetSum": 10
})

# O(log n) O(1)

def twoNumberSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1
        else:
            return [array[left], array[right]]
    return []

twoNumberSum(**{
  "array": [3, 5, -4, 8, 11, 1, -1, 6],
  "targetSum": 10
})