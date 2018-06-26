for i in range(int(input())):
    n, m = input().split()
    n, m = int(n), int(m)
    if (n*m)%2 == 0:
        print("Yes")
    else:
        print("No")
"""
max cuts = n*m-1
""""
