for i in range(int(input())):
    n = input()
    gestures = input()
    if 'I' in gestures:
        print("INDIAN")
    elif 'Y' in gestures:
        print("NOT INDIAN")
    else:
        print("NOT SURE")
