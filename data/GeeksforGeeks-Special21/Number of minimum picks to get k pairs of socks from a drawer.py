def find_min(a,n,k):
    s=0
    complete_pairs=0
    
    for i in range(n):
        complete_pairs += a[i] // 2

        if a[i] % 2 == 0:
            s += ( a[i] - 2 )//2
        else:
            s += ( a[i] - 1 )//2

    if k > complete_pairs:
        return -1

    if k<=s:
        return 2*(k-1) + n + 1

    return 2*s + n + (k-s);    

for _ in range(0,int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    k = int(input())
    
    print(find_min(a,n,k))