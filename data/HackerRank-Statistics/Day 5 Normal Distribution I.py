import math

q1 = 1/2 * (1 + math.erf((19.5 - 20)/(math.sqrt(2)*2)))
q2 = (1/2 * (1 + math.erf((22 - 20)/(math.sqrt(2)*2)))) - 1/2
print(round(q1, 3))
print(round(q2, 3))
