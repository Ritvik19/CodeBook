for t in range(int(input())):
    points_table = {}
    for i in range(12):
        result = input().split()
        team1 = result[0]
        goals1 = int(result[1])
        goals2 = int(result[3])
        team2 = result[4]
        goaldiff1 = goals1-goals2
        if team1 not in points_table.keys():
            points_table[team1] = [0,0]
        if team2 not in points_table.keys():
            points_table[team2] = [0,0]
        if goaldiff1 > 0:
            points_table[team1][0] += 3
            points_table[team2][0] += 0
        elif goaldiff1 < 0:
            points_table[team1][0] += 0
            points_table[team2][0] += 3
        else:
            points_table[team1][0] += 1
            points_table[team2][0] += 1
        points_table[team2][1] -= goaldiff1
        points_table[team1][1] += goaldiff1

        # print(points_table)

    i = 0
    for k in sorted(points_table.items(), key = lambda kv:(kv[1][0], kv[1])[1], reverse=True):
        print(k[0], end=' ')
        i += 1
        if i == 2:
            break
