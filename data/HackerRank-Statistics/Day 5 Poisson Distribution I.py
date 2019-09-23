from math import exp
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

mean = 2.5
k = 5
print(round((mean**k)*(exp(-1*mean))/factorial(k), 3))
