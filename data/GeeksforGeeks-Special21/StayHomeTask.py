def StayHomeTask(arr,n,k):
    arr.sort()
    arr.sort(key= lambda x: x%k)
    for e in arr:
        print(e,end=' ')

if __name__ == '__main__':
    tcs =int(input())
    for _ in range(tcs):
        n,k=[int(x) for x in input().split()]
        arr=[int(x) for x in input().split()]
        StayHomeTask(arr,n,k)
        print()