stack_adder = []
stack_popper = []

def stack_pop():
    if len(stack_popper) > 0:
        return stack_popper.pop()
    else:
        while len(stack_adder) > 0:
            stack_popper.append(stack_adder.pop())
        return stack_popper.pop()

for _ in range(int(input())):
    instruction = input()
    
    if instruction[0] == '1':
        stack_adder.append(int(instruction[2:]))
    elif instruction[0] == '2':
        stack_pop()
    elif instruction[0] == '3':
        value = stack_pop()
        print(value)
        stack_popper.append(value)