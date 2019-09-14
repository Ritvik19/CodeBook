cube = lambda x: x**3

def fibonacci(n):
    if n == 0:
        return []
    if n == 1:
        return [0]
    l = [0,1]
    while len(l) < n:
        l.append(l[-1]+l[-2])
    return l

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
