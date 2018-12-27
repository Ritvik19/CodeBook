numerator = 103993
denominator = 33102

remainder = numerator % denominator

places = ""

for i in range(1, 10**6 + 5):
    remainder *= 10
    places += str(remainder // denominator)
    remainder %= denominator

for t in range(int(input())):
    x = int(input())
    if x == 0:
        print("3")
    else:
        print("3." + places[:x])
