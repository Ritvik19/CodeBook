def isMonotonic(array):
    is_increasing = True
    is_decreasing = True
    for i in range(len(array) - 1):
        if array[i] < array[i + 1]:
            is_decreasing = False
        if array[i] > array[i + 1]:
            is_increasing = False

    return is_increasing or is_decreasing
            
