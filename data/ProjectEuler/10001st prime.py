def is_prime(n):
    for i in range(3, int(n**0.5)+1, 2):
        if n%i == 0:
            return False
    return True

count = 1
num = 1
while count < 10001:
    num += 2
    if is_prime(num):
        count += 1

print(num) # 104743
