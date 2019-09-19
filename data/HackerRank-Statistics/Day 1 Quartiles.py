# Enter your code here. Read input from STDIN. Print output to STDOUT
def median(X):
    n = len(X)
    return (X[(n-1)//2]+X[n//2])//2 if n%2 == 0 else X[n//2]
    # return (X[(n-1)//2]+X[n//2])/2 if n%2 == 0 else X[n//2]

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
print(median(arr[:n//2]))
print(median(arr))
print(median(arr[(n+1)//2:]))
