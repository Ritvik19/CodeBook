# Enter your code here. Read input from STDIN. Print output to STDOUT
def median(X):
    n = len(X)
    return (X[(n-1)//2]+X[n//2])/2 if n%2 == 0 else float(X[n//2])

n = int(input())
elements = list(map(int, input().split()))
freq = list(map(int, input().split()))
arr = []
for e, f in zip(elements, freq):
    arr += [e for j in range(f)]
arr.sort()
n=len(arr)
print(median(arr[(n+1)//2:])-median(arr[:n//2]))
