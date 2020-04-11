# Roxy sees everything differently and she's 18 now.
# Input
# A string
# Output
# A string
# Constraints
# The input string is alpha numeric
# Example
# Input:
# keu
# Output:
# ywg

string=input()
s=""
for i in string :
    s=s+(chr(ord(i)^18))
print(s) 
