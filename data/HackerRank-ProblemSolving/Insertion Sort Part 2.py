def insertionSort(ar, i):
    new = sorted(ar[:i+1]) + ar[i+1:]
    return ' '.join(str(k) for k in new)


s = int(input().strip())
ar = list(map(int, input().split()))

for i in range(1, s):
    print(insertionSort(ar, i))
