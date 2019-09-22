def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact

def combination(n, r):
    return factorial(n)/(factorial(n-r)*factorial(r))

b, g = 1.09, 1
p, q = b/(b+g), g/(b+g)
n = 6
prob = 0
for r in range(3, 7):
    prob += combination(n,r)*(p**(r))*(q**(n-r))
print(round(prob, 3))
