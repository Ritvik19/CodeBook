from math import factorial
m=[]

for t in range(int(input())):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    num = A[K-1]
    i = K-1
    j = K-1
    while i < N and A[i] == num:
        i += 1
    while j > -1 and A[j] == num:
        j -= 1
    n = i - j - 1
    
    print(factorial(n)//(factorial(i-K)*factorial(K-1-j)))