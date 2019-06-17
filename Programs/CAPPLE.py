for t in range(int(input())):
    n = int(input())
    trees = list(map(int, input().split()))
    print(len(set(trees)))
