n = int(input())
X = input()
count = 0
for x in X[::-1]:
    if x == '0':
        count += 1
    else:
        break
print(count)
