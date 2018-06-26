for t in range(int(input())):
    A = [int(e) for e in input().split()]
    crct = A.count(1)
    if crct == 0:
        print("Beginner")
    if crct == 1:
        print("Junior Developer")
    if crct == 2:
        print("Middle Developer")
    if crct == 3:
        print("Senior Developer")
    if crct == 4:
        print("Hacker")
    if crct == 5:
        print("Jeff Dean")
