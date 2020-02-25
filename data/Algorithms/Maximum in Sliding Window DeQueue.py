from DeQueue import DeQueue

def printMax(arr, n, k):
    Qi = DeQueue()
    for i in range(k):
        while (not Qi.isEmpty()) and arr[i] >= arr[Qi.peakRear()]:
            Qi.dequeueFront()
        Qi.enqueueRear(i)

    for i in range(k, n):
        print(str(arr[Qi.peakFront()]) + " ", end="")
        while Qi and Qi.peakFront() <= i-k:
            Qi.dequeueFront()
        while (not Qi.isEmpty()) and arr[i] >= arr[Qi.peakRear()]:
            Qi.dequeueFront()
        Qi.enqueueRear(i)
    print(str(arr[Qi.peakFront()]))

if __name__ == "__main__":
    arr = [12, 1, 78, 90, 57, 89, 56]
    k = 3
    printMax(arr, len(arr), k)
