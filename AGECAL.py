for t in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    A.insert(0,0)
    yb, mb, db = map(int, input().split())
    yc, mc, dc = map(int, input().split())
    sumc = ((yc-1)*sum(A)) + ((yc-1)//4) + sum(A[:mc]) + dc
    sumb = ((yb-1)*sum(A)) + ((yb-1)//4) + sum(A[:mb]) + db
    print(sumc-sumb+1)
