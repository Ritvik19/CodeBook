for i in range(int(input())):
    a, b, c = input().split(" ")
    if int(a) == 0 or int(b) == 0 or int(c) == 0 or int(a)+int(b)+int(c) != 180:
        print("NO")
    else:
        print("YES")
