for t in range(int(input())):
    n = int(input())
    const = list(map(int, input().split()))
    allsum = sum(const)//(n-1)
    variables = []
    for i in range(n):
        variables.append(allsum - const[i])
    print(*variables)
