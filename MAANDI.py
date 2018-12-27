for t in range(int(input())):
    n = int(input())
    count = 0
    for i in range(1, int(n**(0.5))+1):
        if n % i == 0:
            if '4' in str(i) or '7' in str(i):
                count += 1
            if ('4' in str(n//i) or '7' in str(n//i)) and i*i != n:
                count += 1
    print(count)
