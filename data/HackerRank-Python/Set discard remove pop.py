n = int(input())
s = set(map(int, input().split()))
for i in range(int(input())):
    command, *arg = input().split()
    if command == 'pop':
        s.pop()
    if command == 'remove':
        s.remove(int(arg[0]))
    if command == 'discard':
        s.discard(int(arg[0]))
print(sum(s))
