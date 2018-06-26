import re
for i in range(int(input())):
    students = input()
    print(len(re.findall("<>", students)))
