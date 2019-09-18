# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
X = list(map(int, input().split()))
W = list(map(int, input().split()))
weighted_sum = 0
for x, w in zip(X, W):
    weighted_sum += x*w
print(round(weighted_sum/sum(W), 1))
