def bruteForceStringMatching(string, pattern):
    n = len(string)
    m = len(pattern)
    if not pattern:
        return 0
    for i in range(n-m+1):
        si = i
        pi = 0
        while si < n and pi < m and string[si] == pattern[pi]:
            si += 1
            pi += 1
        if pi == m:
            return i
    return -1


if __name__ == '__main__':
    print(bruteForceStringMatching('xyzabcxyz', 'abc'))
