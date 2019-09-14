# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(map(int, input().split()))
flag = True
for _ in range(int(input())):
    B = set(map(int, input().split()))
    flag &= (A.issuperset(B)&(A!=B))
print(flag)
