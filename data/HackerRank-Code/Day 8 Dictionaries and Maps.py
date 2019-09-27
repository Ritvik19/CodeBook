data = dict()
for i in range(int(input())):
    k, v = input().split()
    data[k] = v
while True:
    try:
        k = input()
    except EOFError:
        break
    if k in data.keys():
        print(k, data[k], sep='=')
    else:
        print('Not found')
