def difference(a, b):
    return (ord(a) - ord(b))%26

for t in range(int(input())):
    word  = input()
    n = len(word)
    instructions = 2
    for i in range(1, n):
        instructions += 1 + difference(word[i], word[i-1])
    print('YES') if instructions <= 11*n else print('NO')    
