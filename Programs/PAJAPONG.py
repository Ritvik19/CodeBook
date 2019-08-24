for t in range(int(input())):
    x, y, z = map(int, input().split())
    print('Paja') if ((x+y)//z) %2 == 1 else print('Chef')
