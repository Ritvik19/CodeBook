for t in range(int(input())):
    n = int(input())
    s = input()
    count = 0
    for i in range(n-1):
        if s[i] not in 'aeiou' and s[i+1] in 'aeiou':
            count += 1
    print(count)
