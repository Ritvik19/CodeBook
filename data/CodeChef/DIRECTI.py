for t in range(int(input())):
    n = int(input())
    dir = []
    for i in range(n):
        dir.append(input())
    rev = []
    turn = "Begin"
    for i in range(n):
        temp = dir[-i-1].split()
        newdir = turn + " " + " ".join(e for e in temp[1:])
        if temp[0] == "Left":
            turn = "Right"
        else:
            turn = "Left"
        rev.append(newdir)
    for r in rev:
        print(r)
