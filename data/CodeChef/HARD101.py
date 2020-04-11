# Sort the array.
# Input
# An array
# Output
# An array
# Constraints
# The input array is integer only and has even number of elements.
# Example
# Input:
# 4 2 7 23 66 97 24 989 13 91 213 80 234 45 65 90 12 21
# Output:
# 2 4 7 12 13 21 23 24 65 45 66 80 90 91 97 213 234 989

l = list(map(int,input().split()))
l.sort()
mid = len(l)//2
l[mid],l[mid-1] = l[mid-1],l[mid]
print(*l) 
