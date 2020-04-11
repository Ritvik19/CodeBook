for t in range(int(input())):
    n = int(input())
    sal = list(map(int, input().split()))
    print(sum(sal)-n*min(sal))
