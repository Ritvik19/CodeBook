for t in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    avg = sum(A)/n
    print(A.index(avg)+1) if avg in A else print('Impossible')
