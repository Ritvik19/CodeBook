for i in range(int(input())):
    p = int(input())
    op = 0
    if p >= 2048:
        op += p//2048
        p %= 2048
    for ch in str(bin(p)):
        if ch == '1':
            op += 1
    print(op)    
