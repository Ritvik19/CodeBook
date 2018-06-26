def validate(routine):
    flag = "C"
    for r in routine:
        if flag == "C":
            if r == "E":
                flag = "E"
            if r == "S":
                flag = "S"
        if flag == "E":
            if r == "C":
                return "no"
            if r == "S":
                flag = "S"
        if flag == "S":
            if r == "C":
                return "no"
            if r == "E":
                return "no"
    return "yes"
for t in range(int(input())):
    routine = input()
    print(validate(routine))
