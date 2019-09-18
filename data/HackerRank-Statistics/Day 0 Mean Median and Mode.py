# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
mean = sum(arr)/len(arr)
median = arr[n//2] if n%2 != 0 else (arr[n//2]+arr[(n//2)-1])/2
counts = dict()
for p in arr:
    if p not in counts.keys():
        counts[p] = 0
    counts[p] += 1
mode = list(sorted(sorted(counts.items(), key=lambda x: x[0]), key=lambda x : x[1], reverse=True))[0][0]
print(mean, median, mode, sep='\n')
