for t in range(int(input())):
    n = int(input())
    speed = [int(e) for e in input().split()]
    mov = [speed[0]]
    for i in range(1,n):
        mov.append(min(speed[i], mov[i-1]))
    count = 0
    for a,b in zip(mov, speed):
        if a == b:
            count += 1
    print(count)
