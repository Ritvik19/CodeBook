for i in range(int(input())):
    r = int(input())
    pos1x, pos1y = input().split(" ")
    pos2x, pos2y = input().split(" ")
    pos3x, pos3y = input().split(" ")
    dist = [0, 0, 0]
    dist[0] = ((int(pos1x)-int(pos2x))**2 + (int(pos1y)-int(pos2y))**2)**(0.5)
    dist[1] = ((int(pos2x)-int(pos3x))**2 + (int(pos2y)-int(pos3y))**2)**(0.5)
    dist[2] = ((int(pos3x)-int(pos1x))**2 + (int(pos3y)-int(pos1y))**2)**(0.5)
    if (dist[0] <= r and dist[1] <= r) or (dist[1] <= r and dist[2] <= r) or (dist[2] <= r and dist[0] <= r):
        print("yes")
    else:
        print("no")
