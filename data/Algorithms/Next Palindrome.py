def generateNextPalindromeUtil (num, n) : 
    mid = n//2
    leftsmaller = False
    i = mid - 1
    j = mid + 1 if (n % 2) else mid  

    while (i >= 0 and num[i] == num[j]) : 
        i-=1
        j+=1

    if ( i < 0 or num[i] < num[j]):  
        leftsmaller = True

    while (i >= 0) : 
        num[j] = num[i]  
        j+=1
        i-=1

    if (leftsmaller == True) : 
        carry = 1
        i = mid - 1
        
        if (n%2 == 1) : 
            num[mid] += carry  
            carry = num[mid] // 10 
            num[mid] %= 10
            j = mid + 1

        else: 
            j = mid  

        while (i >= 0) : 
            num[i] += carry  
            carry = num[i] // 10
            num[i] %= 10
            num[j] = num[i]
            j+=1
            i-=1
    return num

def generateNextPalindrome(num, n ) : 
    num  [1]
    if( AreAll9s( num, n ) == True) : 
        for i in range(1, n):  
            num.append(0)  
        num.append(1)  
    else: 
        num = generateNextPalindromeUtil ( num, n )  
    return num  

def AreAll9s(num, n ):  
    for i in range(1, n): 
        if( num[i] != 9 ) : 
            return 0
    return 1

if __name__ == "__main__": 
    num = [9, 4, 1, 8, 7, 9, 7, 8, 3, 2, 2] 
    n = len(num) 
    print("Next palindrome is:",*generateNextPalindrome(num, n))