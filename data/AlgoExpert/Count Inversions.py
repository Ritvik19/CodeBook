def countInversions(array):
    return count_sub_array_inversions(array, 0, len(array))

def count_sub_array_inversions(array, beg, end):
    if end - beg <= 1:
        return 0
    mid = beg + (end - beg) // 2
    l_inversions = count_sub_array_inversions(array, beg, mid)
    r_inversions = count_sub_array_inversions(array, mid, end)
    merged_array_inversions = merge_sort_and_count_inversions(array, beg, mid, end)
    return l_inversions + merged_array_inversions + r_inversions

def merge_sort_and_count_inversions(array, beg, mid, end):
    sorted_array = []
    l = beg
    r = mid
    inversions = 0

    while l < mid and r < end:
        if array[l] <= array[r]:
            sorted_array.append(array[l])
            l += 1
        else:
            inversions += mid - l
            sorted_array.append(array[r])
            r += 1

    sorted_array += array[l:mid] + array[r:end]
    for idx, num in enumerate(sorted_array):
        array[beg + idx] = num

    return inversions
