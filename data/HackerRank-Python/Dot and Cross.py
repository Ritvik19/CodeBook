# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
n = int(input())
A = numpy.array([list(map(int, input().split())) for i in range(n)])
B = numpy.array([list(map(int, input().split())) for i in range(n)])
print(numpy.matmul(A,B))
