# Enter your code here. Read input from STDIN. Print output to STDOUT
def is_prime(n):
    if n < 2:
        return 'Not prime'
    if n == 2:
        return 'Prime'
    else:
        if n %2 == 0:
            return 'Not prime'
        else:
            for i in range(3, int(n**0.5)+1):
                if n%i == 0:
                    return 'Not prime'
            return 'Prime'

for t in range(int(input())):
    print(is_prime(int(input())))
