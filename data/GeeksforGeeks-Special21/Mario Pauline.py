def isPossible(sx, sy, dx, dy):
    if (sx > dx or sy > dy): 
        return False
    if sx == dx and sy == dy:
        return True
    return isPossible(sx, sx+sy, dx, dy) or isPossible(sx+sy, sy, dx, dy)

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        sx,sy,dx,dy = [int(x) for x in input().split()] 
        if (isPossible(sx, sy, dx, dy)): 
            print("True") 
        else: 
            print("False") 