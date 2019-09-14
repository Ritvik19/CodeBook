for i in range(int(input())):
    n, k = input().split()
    n, k = int(n), int(k)
    words = input().split()
    phrases = []
    for j in range(k):
        phrases.append(input().split())
    op = []
    for w in words:
        op.append("NO")
        for j in range(k):
            if w in phrases[j]:
                op[words.index(w)] = "YES"
    print(" ".join(str(o) for o in op))
