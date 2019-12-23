for t in range(int(input())):
    n = int(input())
    marks = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
    for i in range(n):
        p, s = map(int, input().split())
        if p <= 8:
            marks[p] = max(marks[p], s)
    score = 0
    for i in range(1,9):
        score += marks[i]
    print(score)
