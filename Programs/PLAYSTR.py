for t in range(int(input())):
    n = int(input())
    s = input()
    r = input()
    print('YES') if s.count('1') == r.count('1') else print('NO')
