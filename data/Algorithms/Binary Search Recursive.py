def binarySearch(arr, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)
        else:
            return binarySearch(arr, mid + 1, r, x)
    else:
        return -1

if __name__ == "__main__":
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    a = 7
    print(f"{a} found at index {binarySearch(A,0,len(A)-1,a)}")
