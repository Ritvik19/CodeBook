l1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
l2 = ['1', '2', '3', '4', '5', '6', '7', '8']
for t in range(int(input())):
    mov = input()
    if len(mov) != 5 or mov[0] not in l1 or mov[1] not in l2 or mov[2] != "-" or mov[3] not in l1 or mov[4] not in l2:
        print("Error")
    else:
        x = abs(l1.index(mov[0]) - l1.index(mov[3]))
        y = abs(l2.index(mov[1]) - l2.index(mov[4]))
        if x > 2 or y >2 or x+y != 3:
            print("No")
        else:
            print("Yes")
