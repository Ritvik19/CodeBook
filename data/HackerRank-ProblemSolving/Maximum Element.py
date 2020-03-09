stack = [0]
for _ in range(int(input())):
    t, *x = input().split()
    if t == '1':
        x = int(x[0])
        stack.append(max(x, stack[-1]))
    elif t == '2':
        stack.pop(-1)
    else:
        print(stack[-1])
