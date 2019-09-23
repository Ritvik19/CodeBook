import math
mu = 70
sigma = 10
q1 = 1 - (.5 * (1 + math.erf((80 - mu)/(math.sqrt(2)*sigma))))
q2 = 1 - (.5 * (1 + math.erf((60 - mu)/(math.sqrt(2)*sigma))))
q3 = .5 * (1 + math.erf((60 - mu)/(math.sqrt(2)*sigma)))

print(round(100*q1, 2))
print(round(100*q2, 2))
print(round(100*q3, 2))
