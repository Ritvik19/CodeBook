for t in range(int(input())):
    n = int(input())
    A = [int(e) for e in input().split()]
    print(n - len(set(A)))
        
