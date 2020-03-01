def getNextGap(gap):
    gap = (gap * 10)/13
    if gap < 1:
        return 1
    return int(gap)

def combSort(arr):
    n = len(arr)
    gap = n
    swapped = True

    while gap != 1 or swapped == 1:
        gap = getNextGap(gap)
        swapped = False

        for i in range(0, n-gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True

if __name__ == '__main__':
    arr = [8, 4, 1, 3, -44, 23, -6, 28, 0]
    combSort(arr)
    print("Sorted array:", *arr)
