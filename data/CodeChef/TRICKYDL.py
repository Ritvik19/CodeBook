power = [2**i for i in range(37)]
a = [(2**i)-1 for i in range(1, 38)]

for t in range(int(input())):
	A=int(input())
	d1 =0
	d2=0
	for i in range(1,37):
		if(A*(i+1) <= a[i]):
			d1 = i
			break

	for i in range(37):
		if(A<=power[i]):
			d2=i
			break
	print(d1,d2)
