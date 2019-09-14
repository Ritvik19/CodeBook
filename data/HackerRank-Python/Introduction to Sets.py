def average(array):
    ar = set(array)
    return sum(ar)/len(ar)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
