for i in range(int(input())):
    n, m = input().split()
    n, m = int(n), int(m)
    score = (n-1) + (m-1) + ((n-1)*(m-1)*2)
    print(score)
