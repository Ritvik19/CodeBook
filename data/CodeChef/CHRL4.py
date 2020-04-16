n, k = map(int, input().split())
A = list(map(int, input().split()))
minw = [[A[0] ,0]]
j = 1
while j < n:
    if j - k > minw[0][1]:
        minw.pop(0)
    temp = minw[0][0] * A[j]
    while minw[-1][0] > temp and len(minw) != 0:
        minw.pop(-1)
    minw.append([temp, j])
    j += 1
print(minw[-1][0] % 1000000007)