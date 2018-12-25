def count3(x):
    cnt = 0
    while x != 0:
        if x%10==3:
            cnt += 1
        x//=10
    return cnt

for t in range(int(input())):
    n = int(input())
    while True:
        n+=1
        if count3(n) >= 3:
            print(n)
            break
