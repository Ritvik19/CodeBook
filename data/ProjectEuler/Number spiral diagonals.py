sum_ = 1
i = 1
incrementer = 2
count = 0
while i <= 1001*1001:
    i += incrementer
    sum_ += i
    if count %4 == 0:
        incrementer += 2
    count += 1
print(sum_)
