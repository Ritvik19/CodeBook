def mergeSort(array):
    if len(array) == 1:
        return array
    mid_idx = len(array) // 2
    left_half = array[:mid_idx]
    right_half = array[mid_idx:]
    return merge_sort(mergeSort(left_half), mergeSort(right_half))

def merge_sort(left_half, right_half):
    sorted_array = [None] * (len(left_half) + len(right_half))
    k = i = j = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            sorted_array[k] = left_half[i]
            i += 1
        else:
            sorted_array[k] = right_half[j]
            j += 1
        k += 1
    while i < len(left_half):
        sorted_array[k] = left_half[i]
        i += 1
        k += 1
    while j < len(right_half):
        sorted_array[k] = right_half[j]
        j += 1
        k += 1
    return sorted_array