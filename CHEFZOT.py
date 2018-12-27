# import pdb
n = int(input())
arr = [int(e) for e in input().split()]
zer = [-1]
for i in range(n):
    if arr[i] == 0:
        zer.append(i)
zer.append(n)
# pdb.set_trace()
diff = []
for i in range(1,len(zer)):
    diff.append(zer[i]-zer[i-1])
# pdb.set_trace()
print(max(diff)-1)
