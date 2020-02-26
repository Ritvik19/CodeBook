def unorderedLinearSearch(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

if __name__ == "__main__":
    A = [1, 9, 2, 8, 3, 7, 4, 6, 5]
    a = 7
    print(f"{a} found at index {unorderedLinearSearch(A,a)}")
