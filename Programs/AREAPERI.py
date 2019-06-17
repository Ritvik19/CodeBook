l = int(input())
b = int(input())
area = l*b
peri = 2*(l+b)
if l*b > 2*(l+b):
    print("Area")
    print(area)
else:
    print("Peri")
    print(peri)    
