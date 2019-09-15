mport numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    l = list(map(float, arr))
    return numpy.array(l[::-1])

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
