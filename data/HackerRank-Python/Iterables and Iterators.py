def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

def combination(n, k):
    return factorial(n)//(factorial(n-k)*factorial(k))

n = int(input())
s = input().split()
a = s.count('a')
k = int(input())
if s == ['a']:
    print(1.000000000000)
else:
    print(1-round(combination(n-a, k)/combination(n, k), 4))
