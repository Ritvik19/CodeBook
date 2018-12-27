n = int(input())
alpha_ana = [0]*26
strings = []
for i in range(n):
    strings.append(input().strip())

for i in range(26):
    alpha_string = [0]*n
    for j in range(n):
        alpha_string[j] = strings[j].count(chr(97+i))
    alpha_ana[i] = min(alpha_string)

anagram = ''
for i in range(26):
    anagram += alpha_ana[i]*chr(97+i)
if len(anagram) != 0:
    print(anagram)
else:
    print("no such string")
