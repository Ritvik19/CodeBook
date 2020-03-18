def solve(l):
    count = 0
    for i in range(len(l)):
        if l[i] == 0:
            count += 1
        else:
            l[i], l[i-count] = l[i-count], l[i]

if __name__ == '__main__':
    l = [0,1,0,3,12, 0, 9, 0]
    print(l)
    solve(l)
    print(l)