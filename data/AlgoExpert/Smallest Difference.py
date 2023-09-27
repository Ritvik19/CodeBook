def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    idx_one = 0
    idx_two = 0
    smallest_diff = float("inf")
    current_diff = float("inf")
    smallest_pair = []
    while idx_one < len(arrayOne) and idx_two  < len(arrayTwo):
        a = arrayOne[idx_one]
        b = arrayTwo[idx_two]
        if a < b:
            current_diff = b - a
            idx_one += 1
        elif b < a:
            current_diff = a - b
            idx_two += 1
        else:
            return [a, b]
        if smallest_diff > current_diff:
            smallest_diff = current_diff
            smallest_pair = [a, b]
    return smallest_pair
