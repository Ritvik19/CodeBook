def maxSubsetSumNoAdjacent(array):
    if not len(array):
        return 0
    elif len(array) == 1:
        return array[0]
    a = array[0]
    b = max(array[0], array[1])
    for i in range(2, len(array)):
        a, b = b, max(b, a+array[i])
    return b
