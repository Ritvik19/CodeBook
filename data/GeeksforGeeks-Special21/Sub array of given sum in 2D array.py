def check_in_row(r,n,x):
    sum=0
    start=0
    end=0
    
    while(1):
        if sum == x:
            return True
        if sum > x:
            sum -= r[start]
            start += 1
        else:
            if end == n:
                return False
            sum += r[end]
            end += 1

def is_rectangle_there(arr, n, x):
    sum_arr = [ [ 0 for _ in range(n) ] for _ in range(n) ]
    
    for i in range(n):
        for j in range(i,-1,-1):
            for k in range(n):
                sum_arr[j][k] += arr[i][k]
            
            if check_in_row( sum_arr[j], n, x ) is True:
                return True
    
    return False

t=int(input())
for _ in range(t):
    n = int(input())
    line = input().strip().split()
    arr = [ [ int( line[i*n+j] ) for j in range(n) ] for i in range(n) ]
    x = int(input())
    if is_rectangle_there( arr, n, x) is True:
        print('Yes')
    else:
        print('No')