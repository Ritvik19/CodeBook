for t in range(int(input())):
    name = input().split()
    name[-1] = name[-1].capitalize()
    for i in range(len(name)-1):
        name[i] = name[i][0].capitalize() + "."
    print(*name)
