def is_prime(n):
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

sum_ = 2
for i in range(3, 2_000_001, 2):
    if is_prime(i):
        sum_ += i

print(sum_) # 142913828922
