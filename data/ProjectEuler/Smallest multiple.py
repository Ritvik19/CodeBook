from math import gcd

lcm = 1
for i in range(1, 21):
	lcm *= i // gcd(i, lcm)
print(lcm) # 232792560
