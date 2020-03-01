def ternarySearch(arr, l, r, x):
    if (r >= l):
        mid1 = l + (r - l)//3
        mid2 = mid1 + (r - l)//3

        if arr[mid1] == x:
            return mid1

        if arr[mid2] == x:
            return mid2

        if arr[mid1] > x:
            return ternarySearch(arr, l, mid1-1, x)

        if arr[mid2] < x:
            return ternarySearch(arr, mid2+1, r, x)
        return ternarySearch(arr, mid1+1, mid2-1, x)
    return -1

if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    n = len(arr)
    x = 40
    print(x, "is at index", ternarySearch(arr, 0, n-1, x))
