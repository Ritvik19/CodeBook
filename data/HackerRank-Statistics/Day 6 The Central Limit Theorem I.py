import math
weight = 9800
boxes = 49
mean = 205
stdDev = 15
adjustedMean = 49*205
adjustedStdDev = math.sqrt(49) * 15
ans = 1/2 * (1 + math.erf((weight - adjustedMean)/(adjustedStdDev * math.sqrt(2))))
print(round(ans, 4))
