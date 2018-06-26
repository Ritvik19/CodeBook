def divisor(nums):
    for j in range(min(nums),0,-1):
        div = j
        count = 0
        for k in nums:
            if k%j != 0:
                break
            else:
                count += 1
        if count == len(nums):
            return(div)
# print(divisor([4, 4]))

for i in range(int(input())):
    inp = [int(e) for e in input().split()]
    N = inp[0]
    ing = inp[1:]
    div = divisor(ing)
    op = []
    for j in ing:
        op.append(j // div)
    print(" ".join(str(e) for e in op))
