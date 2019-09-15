# Enter your code here. Read input from STDIN. Print output to STDOUT
p = list(map(float, input().split()))
x = float(input())
y = 0
for i in range(len(p)):
    y += p[-i-1]*(x**i)
print(y)
