def kadane(arr):
    n = len(arr)
    maxend = arr[0]
    maxi = arr[0]
    
    for i in range(1,n):
        maxend = max(maxend + arr[i], arr[i])
        maxi = max(maxi, maxend)
    return maxi

def reverseKadane(arr,num):
    sum = 0
    for i in range(num):
        sum += arr[i]
    min_minus = 0
    maxi = sum
    for i in range(num):
        min_minus = min(min_minus + arr[i], arr[i])
        if min_minus == sum:
            return -999999
        maxi = max(maxi, sum - min_minus)
    
    return maxi
        
def maxMoney(arr,n):
    k = kadane(arr)
    rk = reverseKadane(arr,n)
    return max(k,rk)

import math

def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            print(maxMoney(arr,n))
            
            T-=1

if __name__ == "__main__":
    main()
