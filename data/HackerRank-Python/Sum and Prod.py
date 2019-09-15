import numpy
n, m = map(int, input().split())
A = []
for i in range(n):
    A.append(list(map(int, input().split())))
A = numpy.array(A)
B = numpy.sum(A, axis = 0)
print(numpy.prod(B))
