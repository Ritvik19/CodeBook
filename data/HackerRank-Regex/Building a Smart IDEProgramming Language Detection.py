code = input()
while True:
    try:
        code += "\n" + input()
    except:
        break

if 'import java' in code:
    print("Java")
elif '#include' in code:
    print("C")
else:
    print("Python")
