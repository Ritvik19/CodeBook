def interpolationSearch(arr, x):
    lo = 0
    hi = len(arr) - 1
    while lo <= hi and x >= arr[lo] and x <= arr[hi]:
        if lo == hi:
            if arr[lo] == x:
                return lo
            return -1
        pos = lo + \
            int(((float(hi - lo) / (arr[hi] - arr[lo])) * (x - arr[lo])))
        if arr[pos] == x:
            return pos
        if arr[pos] < x:
            lo = pos + 1
        else:
            hi = pos - 1
    return -1

if __name__ == "__main__":
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    a = 7
    print(f"{a} found at index {interpolationSearch(A,a)}")
