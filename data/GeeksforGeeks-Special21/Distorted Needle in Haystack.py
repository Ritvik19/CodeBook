def isShuffledSubstring(needle, haystack): 
    n = len(needle) 
    m = len(haystack) 
    if (n > m): 
        return False
    else: 
        needle = sorted(needle) 

        for i in range(m): 
            if (i + n - 1 >= m): 
                return False
            Str = "" 
            for j in range(n): 
                Str += (haystack[i + j]) 
            Str = sorted(Str) 
            if (Str == needle): 
                return True

if __name__ == '__main__': 
	
	t = int(input())
	for _ in range(t):
		needle = input()
		haystack = input()

		if (isShuffledSubstring(needle,haystack)): 
			print("Yes") 
		else: 
			print("No") 
