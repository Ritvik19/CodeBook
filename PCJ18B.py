def sq_odd(n):
    if n == 0 or n == 1:
        return n
    else:
        return (n*n + sq_odd(n-2))

for t in range(int(input())):
    print(sq_odd(int(input())))
