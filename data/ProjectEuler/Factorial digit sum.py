fact = 1
for i in range(1, 101):
    fact *= i

sod = 0
for d in str(fact):
    sod += int(d)
print(sod) # 648
