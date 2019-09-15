import numpy

size = tuple(map(int, input().split()))
print(numpy.zeros(size, dtype = numpy.int))
print(numpy.ones(size, dtype = numpy.int))
