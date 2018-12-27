for t in range(int(input())):
    S = input()
    n = len(S)
    robo_map = [0]*n
    for i, s in zip(range(n), S):
        if s != '.':
            s = int(s)
            for j in range(max(0, i-s), min(n-1, i+s)+1):
                robo_map[j] += 1
    flag = 'safe'
    for r in robo_map:
        if r > 1:
            flag = 'unsafe'
            break
    print(flag)
