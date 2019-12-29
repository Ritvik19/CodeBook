n, k = map(int, input().split())
opened = [0]*n
for i in range(k):
    query = input()
    if query == 'CLOSEALL':
        opened = [0]*n
    else:
        query = int(query[6:]) - 1
        opened[query] = 1-opened[query]
    print(sum(opened))
