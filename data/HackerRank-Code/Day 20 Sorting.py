import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here

total = 0
for i in range(n):
    numberOfSwaps = 0;
    for j in range(n-1):
        if (a[j] > a[j+1]):
            a[j], a[j+1] = a[j+1], a[j]
            numberOfSwaps += 1
            total += 1
    if (numberOfSwaps == 0):
        break

print(f'Array is sorted in {total} swaps.')
print(f'First Element: {a[0]}')
print(f'Last Element: {a[-1]}')
