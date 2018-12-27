def payup(set, n, sum):
    if sum == 0:
        return True
    if n == 0 and sum != 0:
        return False

    if set[n-1] > sum:
        return payup(set, n-1, sum)

    return payup(set, n-1, sum) or payup(set, n-1, sum-set[n-1])


for t in range(int(input())):
    n, m = map(int, input().split())
    notes = []
    for i in range(n):
        notes.append(int(input()))
    if(payup(notes, n, m)):
        print("Yes")
    else:
        print("No")
