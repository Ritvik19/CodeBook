n, h = input().split(" ")
n, h = int(n), int(h)
status = [int(e) for e in input().split(" ")]
instructions = [int(e) for e in input().split(" ")]
currentstack = 0
box_on_crane = 0

for command in instructions:
    if command == 1:
        if currentstack >0:
            currentstack -=1
    if command == 2:
        if currentstack <n-1:
            currentstack +=1
    if command == 3:
        if status[currentstack] > 0 and box_on_crane == 0:
            box_on_crane = 1
            status[currentstack] -= 1
    if command == 4:
        if status[currentstack] < h and box_on_crane == 1:
            box_on_crane = 0
            status[currentstack] += 1
    if command == 0:
        print(" ".join(str(e) for e in status))
