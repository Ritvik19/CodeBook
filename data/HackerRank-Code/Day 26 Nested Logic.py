def calculate_fine(actual,expected):
    # year:
    if actual[2] > expected[2]:
        return 10000
    elif actual[2] < expected[2]:
        return 0
    else:
        # month
        if actual[1] > expected[1]:
            return 500 * (actual[1]-expected[1])
        elif actual[1] < expected[1]:
            return 0
        else:
            # day
            if actual[0] > expected[0]:
                return 15 * (actual[0]-expected[0])
            else:
                return 0


actual = input().split()
expected = input().split()
for i in range(3):
    actual[i] = int(actual[i])
    expected[i] = int(expected[i])

print(calculate_fine(actual, expected))
