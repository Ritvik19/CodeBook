for t in range(int(input())):
    n = int(input())
    S = input()
    c = S.count("1")
    print(c*(c+1)//2)
