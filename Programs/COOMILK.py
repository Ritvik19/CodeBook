def instructions(string, size):
    if string[size-1] == "cookie":
        return "NO"
    else:
        for i in range(size-1):
            if string[i] == "cookie" and string[i+1] != "milk":
                return "NO"
        return "YES"
for i in range(int(input())):
    n = int(input())
    S = input().split()
    print(instructions(S, n))
