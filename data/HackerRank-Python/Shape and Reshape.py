# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

ar = list(map(int, input().split()))
ar = np.array(ar)
print(ar.reshape((3,3)))
