# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
A = set(map(int, input().split()))

for i in range(int(input())):
    com, arg = input().split()
    B = set(map(int, input().split()))
    if com == 'update':
        A |= B
    if com == 'intersection_update':
        A &= B
    if com == 'symmetric_difference_update':
        A ^= B
    if com == 'difference_update':
        A -= B
print(sum(A))
