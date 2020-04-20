low = 1
high = 1001
mid = (low + high) // 2

while low + 1 != high:
	print('?', mid, 0)
	k = input()
	if k == 'YES':
		low = mid
	else:
		high = mid
	mid = (low + high) // 2
a = mid

low = a
high = 1001
mid = (low + high) // 2

while low + 1 != high:
	print('?', mid, a*2)
	k = input()
	if k == 'YES':
		low = mid
	else:
		high = mid
	mid = (low + high) // 2
base = mid

low = 2 * a
high = 1001
mid = (low + high) // 2

while low + 1 != high:
	print('?', 0, mid)
	k = input()
	if k == 'YES':
		low = mid
	else:
		high = mid
	mid = (low + high) // 2
height = mid-(2*a)

area = base * height + (a * a * 4)
print('!',area)