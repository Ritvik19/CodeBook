for t in range(int(input())):
    n = int(input())
    C = list(map(int, input().split()))
    for i in range(n-2):
        if C[i] == C[i+1] == C[i+2]:
            print("Yes")
            break
    else:
        print("No")
