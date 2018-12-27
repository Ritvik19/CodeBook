for t in range(int(input())):
    n = int(input())
    if n == 1:
        print(1)
    elif n == 2:
        print(1, 2)
    else:
        turn = 0
        lt0 = n-1
        lt1 = n+1
        seq = [n-1, n, n+1]
        while len(seq) < n:
            if turn == 0:
                turn = 1
                lt0 -= 1
                seq.append(lt0)
            else:
                turn = 0
                lt1 += 1
                seq.append(lt1)
        print(*seq)
