triangular_number = lambda n: (n*(n+1))//2

def num_divisors(n):
	end = int(n**0.5)
	result = sum(2
		for i in range(1, end + 1)
		if n % i == 0)
	if end**2 == n:
		result -= 1
	return result

n = 1
while True:
    num = triangular_number(n)
    if num_divisors(num) > 500:
        print(num) # 76576500
        break
    n += 1
