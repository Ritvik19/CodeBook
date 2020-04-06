for t in range(int(input())):
    arr = list(input())
    stack = []
    maxi = 0
    count = 0
    
    for i in range(len(arr)):
        if arr[i] == '<':
            stack.append(arr[i])
            
        else:
            if len(stack) == 0:
                break
            else:
                stack.pop()
                count += 2
        
        if len(stack) == 0:
            maxi = maxi + count
            count = 0
            
    print (maxi)
