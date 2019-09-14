def correct(original, current):
    n = len(original)
    for i in range(n):
        if original[(i-1)%n]^original[i]^original[(i+1)%n] != current[i]:
            return False
    return True

for t in range(int(input())):
    current = list(input())
    current = [int(e) for e in current]
    original00 = [0,0]
    original01 = [0,1]
    original10 = [1,0]
    original11 = [1,1]
    for i in range(2, len(current)):
        original00.append(original00[i-2]^original00[i-1]^current[1])
        original01.append(original01[i-2]^original01[i-1]^current[1])
        original10.append(original10[i-2]^original10[i-1]^current[1])
        original11.append(original11[i-2]^original11[i-1]^current[1])
    correct00 = correct(original00, current)
    correct01 = correct(original01, current)
    correct10 = correct(original10, current)
    correct11 = correct(original11, current)
    count = correct00 + correct01 + correct10 + correct11
    if count == 0:
        print("No solution")
    elif count == 1:
        if correct00:
            print("".join(str(e) for e in original00))
        elif correct01:
            print("".join(str(e) for e in original01))
        elif correct10:
            print("".join(str(e) for e in original10))
        else:
            print("".join(str(e) for e in original11))
    elif count > 1:
        print("Multiple solutions")
