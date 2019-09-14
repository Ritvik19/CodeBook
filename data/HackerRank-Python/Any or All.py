def is_palindrome(x):
    return str(x) == str(x)[::-1]

def is_positive(x):
    return  x > 0

n = int(input())
A = list(map(int, input().split()))
print(all(map(is_positive, A)) and any(map(is_palindrome, A)))
