def flipBit(n): 
    if (~n == 0): 
        return 8 * sizeof()
        
    currLen = 0
    prevLen = 0
    maxLen = 0
    
    while n > 0: 
        if (n & 1) == 1: 
            currLen += 1
        elif ((n & 1) == 0): 
            prevLen = 0 if((n & 2) == 0) else currLen
            currLen = 0
            
        maxLen = max(prevLen + currLen, maxLen)
        
        n >>= 1
    
    return maxLen + 1

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(flipBit(n))
