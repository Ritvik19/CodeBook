for i in range(int(input())):
    n = int(input())
    A = [int(e) for e in input().split(" ")]
    print(sorted(A)[0]*(len(A)-1))
