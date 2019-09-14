def solve(s):
    S = s.split()
    return ' '.join(s.capitalize() for s in S) + ' '
print(solve(input()))
