# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
n, m = map(int, input().split())
A = []
for i in range(n):
    A.append(list(map(int, input().split())))
A = numpy.array(A)
B = numpy.min(A, axis = 1)
print(numpy.max(B))
