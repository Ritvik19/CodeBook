for i in range(int(input())):
    a, b = input().split()
    a, b = int(a), int(b)
    if abs(a-b) == 2:
        print("YES")
    elif abs(a-b) == 1 and max(a, b)%2 == 0:
        print("YES")
    else:
        print("NO")
