import time

class Memoize:
    def __init__(self, f):
        self.f = f
        self.memo = {}
    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        return self.memo[args]
        
def factorial(k):
    if k < 2: 
        return 1
    
    return k * factorial(k - 1)

def fibonacci(n):
    if n <= 2:
        return n - 1
    
    return fibonacci(n-1) + fibonacci(n-2)

m_factorial = Memoize(factorial)    
m_fibonacci = Memoize(fibonacci)

if __name__ == '__main__':
    print('Factorial:')
    start = time.time()
    print(factorial(500))
    print(f'Time: {time.time() - start}\n')
    
    print('Memoized Factorial:')
    start = time.time()
    print(m_factorial(500))
    print(f'Time: {time.time() - start}\n')

    print('Fibonacci:')
    start = time.time()
    print(fibonacci(40))
    print(f'Time: {time.time() - start}\n')
    
    print('Memoized Fibonacci:')
    start = time.time()
    print(m_fibonacci(40))
    print(f'Time: {time.time() - start}\n')    
    
    