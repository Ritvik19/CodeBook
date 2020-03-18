def solve(l):
    l.sort()
    l_ = [l[0]]
    for i in range(1, len(l)):
        l_.append(l[i])
        if l[i][0] <= l[i-1][1]:
            l_[-2][1] = max(l_[-2][1], l_[-1][1])
            l_.pop(-1)
    return l_


if __name__ == '__main__':
    l = [[1, 3], [5, 8], [4, 10], [15, 21], [20, 25]]
    print(l)
    print(solve(l))
