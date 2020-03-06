def permute(a, l, r, permutations): 
    if l==r: 
        permutations.append(''.join(a)) 
    else: 
        for i in range(l,r+1): 
            a[l], a[i] = a[i], a[l] 
            permute(a, l+1, r, permutations) 
            a[l], a[i] = a[i], a[l]

if __name__ == '__main__':
    string = "ABC"
    n = len(string) 
    permutations = []
    permute(list(string), 0, n-1,permutations) 
    print(*permutations)