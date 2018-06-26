for i in range(int(input())):
    a, b = input().split()
    A = set(int(e) for e in input().split())
    B = set(int(e) for e in input().split())
    print(len(A & B))
