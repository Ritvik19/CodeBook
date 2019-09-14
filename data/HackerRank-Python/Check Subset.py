# Enter your code here. Read input from STDIN. Print output to STDOUT
for t in range(int(input())):
    a = int(input())
    A = set(map(int, input().split()))
    b = int(input())
    B = set(map(int, input().split()))
    print(A.issubset(B))
