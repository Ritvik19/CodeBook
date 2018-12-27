def input_aux(x):
    if x == 'monday': return 0
    elif x == 'tuesday': return 1
    elif x == 'wednesday': return 2
    elif x == 'thursday': return 3
    elif x == 'friday': return 4
    elif x == 'saturday': return 5
    elif x == 'sunday': return 6
    else: return int(x)

for t in range(int(input())):
    s, e, l, r = map(input_aux, input().split())
    duration = (e-s+1)%7
    count = 0
    exact = None
    for week in range(100):
        if l <= duration <= r:
            count += 1
            exact = duration
        duration += 7
    if count == 0:
        print('impossible')
    elif count == 1:
        print(exact)
    else:
        print('many')
