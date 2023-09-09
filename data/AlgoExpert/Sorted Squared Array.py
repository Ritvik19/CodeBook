# O(n) O(n)

def sortedSquaredArray(array):
    sorted_squares = [0 for _ in array]
    left = 0
    right = len(array) - 1

    # filling the array in reverse because the values at extremes are largest
    for i in reversed(range(len(array))):
        left_val = array[left]
        right_val = array[right]

        if abs(left_val) > abs(right_val):
            sorted_squares[i] = (left_val**2)
            left += 1
        else:
            sorted_squares[i] = (right_val**2)
            right -= 1
    return sorted_squares

sortedSquaredArray(**{
  "array": [-10, -5, 0, 5, 10]
})