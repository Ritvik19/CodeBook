# Enter your code here. Read input from STDIN. Print output to STDOUT
n = 5
xArr = [95,85,80,70,60]
yArr = [85,95,70,65,70]
xMean = sum(xArr)/n
yMean = sum(yArr)/n
xVariance = 0
for x in xArr:
    xVariance = xVariance + (x - xMean)**2
xVariance = xVariance * 1/n
xStdDev = xVariance**.5
yVariance = 0
for y in yArr:
    yVariance = yVariance + (y - yMean)**2
yVariance = 1/n * yVariance
yStdDev = yVariance**.5
pearson = 0
for i in range(n):
    pearson = pearson + (xArr[i] - xMean)*(yArr[i] - yMean)
pearson = pearson/(n*xStdDev *yStdDev)
b = pearson * yStdDev / xStdDev
a = yMean - b * xMean
print(round(a + b*80, 3))
