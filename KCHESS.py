for t in range(int(input())) :
    n = int(input())
    knight = []
    for x in range(n):
        knight.append([int(x) for x in input().split()])
    def attack(x,y,knight):
        stat = 0
        knight_attack = []

        knight_attack.append([x+2,y-1])
        knight_attack.append([x+2,y+1])
        knight_attack.append([x-2,y+1])
        knight_attack.append([x-2,y-1])
        knight_attack.append([x+1,y-2])
        knight_attack.append([x+1,y+2])
        knight_attack.append([x-1,y+2])
        knight_attack.append([x-1,y-2])

        for x in range(8):
            if knight_attack[x] in knight:
                stat = 0
                break
            else:
                stat = 1
        return stat

    king = [int(x) for x in input().split()]
    status = [None]*9
    while True :
        status[1] = attack(king[0]+1,king[1]+0,knight)
        status[2] = attack(king[0]-1,king[1]+0,knight)
        status[3] = attack(king[0]+0,king[1]-1,knight)
        status[4] = attack(king[0]-0,king[1]+1,knight)
        status[5] = attack(king[0]+1,king[1]-1,knight)
        status[6] = attack(king[0]+1,king[1]+1,knight)
        status[7] = attack(king[0]-1,king[1]+1,knight)
        status[8] = attack(king[0]-1,king[1]-1,knight)
        break

    print('NO') if 1 in status else print('YES')
