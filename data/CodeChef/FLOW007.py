for i in range(int(input())):
    n = input()
    op = ""
    for ch in n:
        op = ch+op
    print(int(op))
