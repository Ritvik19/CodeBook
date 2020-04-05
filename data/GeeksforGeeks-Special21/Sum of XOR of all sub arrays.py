def sum_of_XOR(arr,n):
    ret=0
    pv=1
    
    for power in range(20):
        count = 0
        odd=0
        even=0

        for i in range(n):
            if arr[i] & pv > 0:
                odd , even = even+1 , odd
                count += odd
            else:
                even += 1
                count += odd
        
        ret += count * pv
        pv=pv<<1
    
    return ret

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        print(sum_of_XOR(arr,n))