def factorial(n):
    fact = 1
    for i in range(n):
         fact *= (i+1)
    return fact

def combination(n, r):
    return factorial(n)//(factorial(r)*factorial(n-r))

print(combination(40, 20)) # 137846528820
