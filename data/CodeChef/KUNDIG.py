from math import factorial
for t in range(int(input())):
    n = int(input())
    A = [int(e) for e in input().split()]
    print(factorial(n-1)*sum(A)*int("1"*n))
