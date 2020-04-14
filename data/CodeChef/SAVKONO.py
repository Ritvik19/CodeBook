for t in range(int(input())):
    n,z = map(int, input().split())
    arr = list(map(int, input().split()))
    
    remains = [0]*10001
    for i in arr:
        remains[i] += 1
    
    res = 0
    ind = 10000
    
    while (z>0):
        if ind<=0:
            break
            
        if remains[ind]==0:
            ind -= 1
            continue
            
        if z<0 or ind<0:
            break
            
        z -= ind
        remains[ind] -= 1
        remains[ind//2] += 1
        res += 1
    
    if z<=0:
        print(res)
    else:
        print("Evacuate")