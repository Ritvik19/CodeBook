for t in range(int(input())):
    d = {}
    for i in range(int(input())):
        
        word, mark = input().split()
        word, mark = str(word),int(mark)
        if word in d:
            d[word][mark] += 1
        else:
            d[word] = [0,0]
            d[word][mark]=1
            
    ans = 0
    for word in d:
        ans += max(d[word])
    print(ans)