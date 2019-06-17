for i in range(int(input())):
    n, v1, v2 = input().split(" ")
    if (2**(0.5))*int(n)/int(v1) < (2*int(n))/int(v2):
        print("Stairs")
    else:
        print("Elevator")
