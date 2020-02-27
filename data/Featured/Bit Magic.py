def kthBit(n, k):
    return bool(n&(1<<k-1))

def setKthBit(n, k):
    return n|(1<<k-1)
    
def clearKthBit(n, k):
    return n&~(1<<k-1)

def toggleKthBit(n, k):
    return n^(1<<k-1)
    
def toggleRightmostBit(n):
    return n&n-1
    
def rightmostOneBit(n):
    return n&-n

def rightmostZeroBit(n):
    return ~n&n+1

def isAPowerOfTwo(n):
    return n&n-1 == 0

def multiplyByPowerOfTwo(n, k):
    return n << k
    
def divideByPowerOfTwo(n, k):
    return n >> k    

def reverseBinary(n):
    rev = 0
    while (n > 0) : 
        rev = rev << 1
        if (n & 1 == 1) : 
            rev = rev ^ 1
        n = n >> 1
    return rev 

def countOne(n):
    count = 0
    while n:
        count += 1
        n &= n-1
    return count

def maskOfTrailingZeros(n):
    return (n&-n)-1
    
if __name__ == '__main__':
    print(kthBit(25, 4)) # 25 => 11001
    print(kthBit(25, 3))
    print(setKthBit(25,3)) # 11101 => 29
    print(clearKthBit(25, 4)) # 10001 => 17
    print(rightmostOneBit(10)) #1010
    print(rightmostZeroBit(10))
    print(isAPowerOfTwo(9))
    print(multiplyByPowerOfTwo(5, 2))
    print(divideByPowerOfTwo(5, 2))
    print(reverseBinary(10)) 
    print(countOne(10))
    print(maskOfTrailingZeros(20)) # 20 => 10100
                                   #  3 => 00011