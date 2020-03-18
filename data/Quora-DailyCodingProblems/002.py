def solve(l):
    if len(l) < 3:
        return None
    l.sort()
    return max(l[-1] * l[-2] * l[-3], l[0]*l[1]*l[-1])


if __name__ == '__main__':
    l = [-4, -4, 2, 8]
    print(l)
    result = solve(l)
    print(result)
