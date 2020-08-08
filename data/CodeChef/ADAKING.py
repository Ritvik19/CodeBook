for t in range(int(input())):
    k = int(input())
    chess = []
    for i in range(64-k):
        chess.append('X')
    for i in range(k-1):
        chess.append('.')
    chess.append('O')
    for i in range(0, 64, 8):
        print(*chess[i:i+8], sep='')