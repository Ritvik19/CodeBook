sum_ = 0
x = 1
y = 2
while x <= 4_000_000:
	if x % 2 == 0:
		sum_ += x
	x, y = y, x + y
print(sum_) # 4613732
