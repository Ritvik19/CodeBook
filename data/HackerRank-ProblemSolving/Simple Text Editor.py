stack = ['']

for _ in range(int(input())):
    t, *arg = input().split()
    if t == '1':
        w = arg[0]
        stack.append(stack[-1]+w)
    elif t == '2':
        k = int(arg[0])
        stack.append(stack[-1][:-k])
    elif t == '3':
        k = int(arg[0])-1
        print(stack[-1][k])
    else:
        stack.pop(-1)
