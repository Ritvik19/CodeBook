def IsArraySorted(arr, n):
    if n == 1:
        return 1
    else:
        return 0 if arr[n-1] < arr[n-2] else IsArraySorted(arr, n-1)


if __name__ == "__main__":
    print(IsArraySorted([1, 5, 2, 4, 3], 5))
