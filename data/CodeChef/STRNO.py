for t in range(int(input())) :
    x, k = map(int, input().split())
    l = []
    while x % 2 == 0: 
        l.append(2) 
        x = x // 2
    for i in range(3, int(x**0.5)+1, 2): 
        while x % i == 0: 
            x = x / i; 
            l.append(i) 
    if x > 2: 
        l.append(x) 
    print(0) if len(l) < k else print(1)