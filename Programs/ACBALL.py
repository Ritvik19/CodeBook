for i in range(int(input())):
    x = input()
    y = input()
    z = ""
    for a,b in zip(x, y):
        if a != b :
            z += "B"
        else:
            if a == "B":
                z += "W"
            else:
                z += "B"
    print(z)
