for t in range(int(input())):
    n, x = map(int, input().split())
    visit_map = set([x])
    current = x
    S = input()
    for s in S:
        if s == 'L':
            current -= 1
        else:
            current += 1
        visit_map = visit_map|set([current])
    print(len(visit_map))
