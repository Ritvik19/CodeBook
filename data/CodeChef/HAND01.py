# Credits: Sir Isaac Newton is standing over a circle of radius 0.5641895835477563.
# Input
# The first line of the input contains an integer T denoting the number of test cases. The next T lines contain a string containing numbers and one or more special charters (?, !, %, $)
# Output
# For each test case, output a single line containing a single real number.
# Constraints
# Should contain all the constraints on the input data that you may have. Format it like:
# 1 ≤ T ≤ 100
# Example
# Input:
# 2
# 3!2?1
# 5%2$2
# Output:
# 5
# 6.0

for t in range (int(input())):
    str1=input()
    a=len(str1)
    b=""
    for i in range (a):
        if(str1[i]=='!'):
            b=b+'*'
        elif(str1[i]=='?'):
            b=b+'-'
        elif(str1[i]=='%'):
            b=b+'+'
        elif(str1[i]=='$'):
            b=b+'/'
        else:
            b=b+str1[i]
    print(eval(b))
