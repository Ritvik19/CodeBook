# O(n) O(1)

def findThreeLargestNumbers(array):
    largest_numbers = [None, None, None]
    for num in array:
        update_largest(largest_numbers, num)
    return largest_numbers

def update_largest(largest_numbers, num):
    if largest_numbers[2] is None or num > largest_numbers[2]:
        shift_and_update(largest_numbers, num ,2)
    elif largest_numbers[1] is None or num > largest_numbers[1]:
        shift_and_update(largest_numbers, num ,1)
    elif largest_numbers[0] is None or num > largest_numbers[0]:
        shift_and_update(largest_numbers, num ,0)


def shift_and_update(array, num, idx):
    for i in range(idx + 1):
        if i == idx:
            array[i] = num
        else:
            array[i] = array[i+1]
            
findThreeLargestNumbers(**{
  "array": [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
})