for t in range(int(input())):
    villages = input()
    l = ""
    A, B, count = villages.count("A"), villages.count("B"), 0
    for v in villages:
        if l == "" and (v == "A" or v == "B"):
            l = v
        if l == "A" or l == "B":
            if v == ".":
                count += 1
            else:
                if v == l:
                    if l == "A":
                        A += count
                    if l == "B":
                        B += count
                l = v
                count = 0
    print(A, B)
