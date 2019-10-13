# Returns the smallest factor of n, which is in the range [2, n]. The result is always prime.
def smallest_prime_factor(n):
	assert n >= 2
	for i in range(2, int(n**0.5) + 1):
		if n % i == 0:
			return i
	return n

# By the fundamental theorem of arithmetic, every integer n > 1 has a unique factorization as a product of prime numbers.
# In other words, the theorem says that n = p_0 * p_1 * ... * p_{m-1}, where each p_i > 1 is prime but not necessarily unique.
# Now if we take the number n and repeatedly divide out its smallest factor (which must also be prime), then the last
# factor that we divide out must be the largest prime factor of n.

NUM = 600851475143
while True:
    p = smallest_prime_factor(NUM)
    if p < NUM:
        NUM //= p
    else:
        print(NUM) # 6857
        break
