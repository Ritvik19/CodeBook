# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
X = list(map(float, input().split()))
Y = list(map(float, input().split()))

meanX = sum(X)/n
DX = list(map(lambda x: (meanX-x)**2, X))
stdX = (sum(DX)/n)**(0.5)

meanY = sum(Y)/n
DY = list(map(lambda x: (meanY-x)**2, Y))
stdY = (sum(DY)/n)**(0.5)

corr = 0
for x, y in zip(X, Y):
    corr += (x-meanX)*(y-meanY)
corr /= n*stdX*stdY
print(round(corr, 3))
