for t in range(int(input())):
    n = int(input())
    S = input()
    U = input()
    score = 0
    i=0
    while i<n:
        if S[i] == U[i]:
            score += 1
        elif U[i] != 'N':
            i += 1
        i += 1
    print(score)
