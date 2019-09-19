# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
X = list(map(int, input().split()))
mean = sum(X)/n
D = list(map(lambda x: (mean-x)**2, X))
std = (sum(D)/n)**(0.5)
print(std)
