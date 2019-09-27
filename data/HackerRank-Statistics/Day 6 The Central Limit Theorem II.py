import math
tickets = 250
students = 100
mean = 2.4
stdDev = 2.0
adjustedMean = 2.4*100
adjustedStdDev = 2*10
ans = 1/2 * (1 + math.erf((tickets - adjustedMean)/(math.sqrt(2)*adjustedStdDev)))
print(round(ans, 4))
