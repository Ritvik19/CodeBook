if __name__ == '__main__':
    N = int(input())
    mini = 101
    mini2 = 102
    a = []
    for i in range(N):
        name = input()
        mark = float(input())
        if mark<mini:
            mini2 = mini
            mini = mark
        elif mark>mini and mark<mini2:
            mini2 = mark
        a.append([name, mark])
    b = [x[0] for x in a if x[1]==mini2]
    b.sort()
    for y in b:
        print(y)
