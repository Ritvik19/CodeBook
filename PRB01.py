def prime(n):
    for i in range(2,n//2):
        if n % i == 0:
            return "no"
    return "yes"

for i in range(int(input())):
    print(prime(int(input())))
