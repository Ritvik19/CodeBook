for t in range(int(input())):
    a, b = map(int, input().split())
    if a %2 == 1 and b %2 == 1:
        print("Vanka")
    else:
        print("Tuzik")
