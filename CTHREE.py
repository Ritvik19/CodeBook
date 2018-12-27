for t in range(int(input())):
    n, a, b, c = map(int, input().split())
    factors = []
    for i in range(1, int(n**(1/2))+1):
        if n % i == 0:
            factors.append(i)
            if i*i != n:
                factors.append(n//i)
    factors.sort()
    count = 0
    for i in factors:
        if i <= a:
            rem = n//i
            for j in factors:
                if j <= b and rem % j == 0:
                    if rem//j <= c:
                        count += 1
    print(count)
