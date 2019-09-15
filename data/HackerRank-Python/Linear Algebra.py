# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
n = int(input())
A = numpy.array([list(map(float, input().split())) for i in range(n)])
print(round(numpy.linalg.det(A),2))
