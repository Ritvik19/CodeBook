for t in range(int(input())):
    n = int(input())
    i = 2
    prime = []
    while(n != 1):
        if n % i == 0:
            n //= i
            if i not in prime:
                prime.append(i)
        else:
            i += 1
    print(*prime)
