from collections import deque
d = deque()
for i in range(int(input())):
    cmd, *arg = input().split()
    if cmd == 'append':
        d.append(int(arg[0]))
    if cmd == 'pop':
        d.pop()
    if cmd == 'popleft':
        d.popleft()
    if cmd == 'appendleft':
        d.appendleft(int(arg[0]))
print(*d)
