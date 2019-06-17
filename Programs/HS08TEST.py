ip = input().split(" ")
x = float(ip[0])
y = float(ip[1])
if x < y-0.50 and x%5==0:
    print(format(y-x-0.50, '.2f'))
else:
    print(format(y, '.2f'))
