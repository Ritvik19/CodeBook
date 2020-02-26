def segregateEvenOdd(arr):
    left, right = 0, len(arr)-1
    while left < right:

        while (arr[left] % 2 == 0 and left < right):
            left += 1

        while (arr[right] % 2 == 1 and left < right):
            right -= 1

        if (left < right):
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right = right-1

if __name__ == "__main__":
    arr = [12, 34, 45, 9, 8, 90, 3]
    segregateEvenOdd(arr)
    print("Array after segregation ")
    print(*arr)
