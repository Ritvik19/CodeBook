# There was a watch.
# Input
# A string
# Output
# A string containing only '!' and '?'
# Constraints
# The input string is a permutation of ['A', 'E', 'L', 'M', 'O', 'R', 'S', 'U']
# Example
# Input:
# LAM
# Output:
# ?!???!!!

# Morsecode

n=input()
s=['?!','?','?!??','!!','!!!','?!?','???','??!']
m=[]
m=n
o=[]
for i in range(len(m)):
    if(m[i]=='A'):
        o.append(s[0])
    elif(m[i]=='E'):
        o.append(s[1])
    elif(m[i]=='L'):
        o.append(s[2])
    elif(m[i]=='M'):
        o.append(s[3])
    elif(m[i]=='O'):
        o.append(s[4])
    elif(m[i]=='R'):
        o.append(s[5])
    elif(m[i]=='S'):
        o.append(s[6])
    elif(m[i]=='U'):
        o.append(s[7])
o=''.join(o)
print(o) 
