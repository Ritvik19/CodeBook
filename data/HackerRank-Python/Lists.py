if __name__ == '__main__':
    l = []
    N = int(input())
    for i in range(N):
        command, *arg = input().split()
        if command == 'insert':
            l.insert(int(arg[0]), int(arg[1]))
        if command == 'print':
            print(l)
        if command == 'remove':
            l.remove(int(arg[0]))
        if command == 'append':
            l.append(int(arg[0]))
        if command == 'sort':
            l.sort()
        if command == 'pop':
            l.pop()
        if command == 'reverse':
            l.reverse() 
