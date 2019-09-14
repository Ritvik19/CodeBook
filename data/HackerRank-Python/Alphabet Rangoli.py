def print_rangoli(size):
    alpha = {}
    for i in range(97, 123):
        alpha[i-96] = chr(i)

    m = (2*n)-1

    for i in range(m//2):
        print('-'*(m-2*i-1), end='')
        for j in range(i):
            print(alpha[n-j]+'-', end='')
        print(alpha[n-i], end='')
        for j in range(i)[::-1]:
            print('-'+alpha[n-j], end='')
        print('-'*(m-2*i-1), end='')
        print()

    for j in range(n-1):
        print(alpha[n-j]+'-', end='')
    print(alpha[1], end='')
    for j in range(n-1)[::-1]:
        print('-'+alpha[n-j], end='')
    print()
    for i in range(m//2)[::-1]:
        print('-'*(m-2*i-1), end='')
        for j in range(i):
            print(alpha[n-j]+'-', end='')
        print(alpha[n-i], end='')
        for j in range(i)[::-1]:
            print('-'+alpha[n-j], end='')
        print('-'*(m-2*i-1), end='')
        print()

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
