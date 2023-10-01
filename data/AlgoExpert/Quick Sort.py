def quickSort(array):
    quick_sort(array, 0, len(array) - 1)
    return array

def quick_sort(array, beg_idx, end_idx):
    if beg_idx >= end_idx:
        return

    pivot_idx = beg_idx
    left_idx = beg_idx + 1
    right_idx = end_idx

    while right_idx >= left_idx:
        if array[left_idx] > array[pivot_idx] and array[right_idx] < array[pivot_idx]:
            swap(left_idx, right_idx, array)
        if array[left_idx] <= array[pivot_idx]:
            left_idx += 1
        if array[right_idx] >= array[pivot_idx]:
            right_idx -= 1
    swap(pivot_idx, right_idx, array)
    left_sub_array_is_smaller = right_idx - 1 - beg_idx < end_idx - (right_idx + 1)
    if left_sub_array_is_smaller:
        quick_sort(array, beg_idx, right_idx - 1)
        quick_sort(array, right_idx + 1, end_idx)
    else:
        quick_sort(array, right_idx + 1, end_idx)
        quick_sort(array, beg_idx, right_idx - 1)

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]