from math import inf
for i in range(int(input())):
    n = input()
    nums = [int(e) for e in input().split(" ")]
    print(sorted(nums)[0]+sorted(nums)[1])
