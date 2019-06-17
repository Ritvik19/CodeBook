for t in range(int(input())):
    score = input()
    C = O = 0
    for s in score:
        if s == '0':
            O += 1
        elif s == '1':
            C += 1
        if C < 10 and O == 11:
            print("LOSE")
            break
        elif O < 10 and C == 11:
            print("WIN")
            break
        elif O >= 10 and C >= 10:
            if C-O == 2:
                print("WIN")
                break
            elif O-C == 2:
                print("LOSE")
                break
