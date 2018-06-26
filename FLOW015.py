day = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
for i in range(int(input())):
    year = int(input())
    d_key = 0

    y1 = (year - 1)//100
    if y1%4 == 3:
        d_key += 1
    if y1%4 == 2:
        d_key += 3
    if y1%4 == 1:
        d_key += 5
    if y1%4 == 0:
        d_key += 0

    y2 = (year -1)%100
    d_key += (y2+y2//4)%7

    print(day[(d_key+1)%7])
