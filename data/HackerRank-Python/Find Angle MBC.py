# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
L = [int(input()) for i in range(2)]
s = str(int(round(math.atan2(*L) / math.pi*180, 0)))
print(s, end='')
print('°')
