for t in range(int(input())):
	n=int(input())
	x,y,z=[],[],[]
	for i in range(n):
		z.append(int(input()))
	print("Case {}:".format(t+1))
	for i in z:
		x.append(i>>16)
		y.append(i-(x[-1]<<16))
	print(*y)
	print(*x)
