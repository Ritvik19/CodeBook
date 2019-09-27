# Enter your code here. Read input from STDIN. Print output to STDOUT
from sklearn import linear_model

m,n = [int(x) for x in input().split(' ')]
x = []
y = []
for i in range(n):
    arr = [float(x) for x in input().split(' ')]
    x.append(arr[:-1])
    y.append(arr[-1])

lm = linear_model.LinearRegression()
lm.fit(x, y)
a = lm.intercept_
b = lm.coef_
q = int(input())
for i in range(q):
    arr = [float(x) for x in input().split(' ')]
    ans = a
    for j in range(m):
        ans = ans + arr[j]*b[j]
    print(round(ans, 2))
