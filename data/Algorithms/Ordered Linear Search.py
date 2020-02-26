def orderedLinearSearch(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
        if arr[i] > x:
            return -1
    return -1

if __name__ == "__main__":
    A = [1,2,3,4,5,6,7,8,9]
    a = 7
    print(f"{a} found at index {orderedLinearSearch(A,a)}")