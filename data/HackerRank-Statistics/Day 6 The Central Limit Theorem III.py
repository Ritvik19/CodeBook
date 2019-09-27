import math
samples = 100
mean = 500
stdDev = 80
stdDev = stdDev / math.sqrt(samples)
interval = .95
z = 1.96
a = -z * stdDev + 500
b = z * stdDev + 500
print(round(a, 2))
print(round(b, 2))
