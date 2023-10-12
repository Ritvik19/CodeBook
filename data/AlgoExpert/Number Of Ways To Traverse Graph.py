def numberOfWaysToTraverseGraph(width, height):
    return factorial(width - 1 + height -1) // (factorial (width - 1) * factorial (height - 1))

def factorial(num):
    res = 1
    for n in range(2, num +1):
        res *= n
    return res