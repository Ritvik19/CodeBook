for t in range(int(input())):
    n = int(input())
    a = []
    for i in range(n):
        a.append(input())
    if n == 0:
        print("Draw")
    elif n == 1:
        print(a[0])
    else:
        teams = [team for team in set(a)]
        goals = [a.count(team) for team in teams]
        if goals[0] > goals[1]:
            print(teams[0])
        elif goals[1] > goals[0]:
            print(teams[1])
        else:
            print("Draw")
