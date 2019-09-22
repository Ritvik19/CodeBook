def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact

def combination(n, r):
    return factorial(n)/(factorial(n-r)*factorial(r))

p, q = 0.12, 0.88
n= 10
prob = 0
for r in range(2+1):
    prob += combination(n,r)*(p**(r))*(q**(n-r))
print(round(prob, 3))
prob = 0
for r in range(2, 10+1):
    prob += combination(n,r)*(p**(r))*(q**(n-r))
print(round(prob, 3))
