def isprime(x):
    for i in range (2, int(x**(0.5))+1):
        if x%i == 0:
            return False
    return True

primes200 = [2]
for i in range(3, 200, 2):
    if isprime(i):
        primes200.append(i)

semiprimes200 = []
num_primes200 = len(primes200)
for i in range(num_primes200):
    for j in range(i+1, num_primes200):
        semiprimes200.append(primes200[i]*primes200[j])

num_semiprimes200 = len(semiprimes200)
sum_semiprimes200 = []
for i in range(num_semiprimes200):
    for j in range(i, num_semiprimes200):
        sum_semiprimes200.append(semiprimes200[i]+semiprimes200[j])

for t in range(int(input())):
    print('YES') if int(input()) in sum_semiprimes200 else print('NO')
