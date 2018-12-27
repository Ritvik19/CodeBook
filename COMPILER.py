for t in range(int(input())):
    str = input()
    count = bal = closed = 0
    for s in str:
        if s == '<':
            bal += 1
        else:
            if bal > 0:
                bal -=1
                closed += 1
                if bal == 0:
                    count += 2*closed
    print(count)
