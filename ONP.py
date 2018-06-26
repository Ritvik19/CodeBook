def peak(stack):
    return stack[len(stack)-1]
def pop(stack):
    return stack[0:(len(stack)-1)]
def precedence(operator):
    if operator == '^':
        return 3
    elif operator == '*' or operator == '/':
        return 2
    elif operator == '+' or operator == '-':
        return 1
    else:
        return 0

def rpn(infix):
    infix += ")"
    stack = "("
    postfix = ""
    print("\t(")
    for char in infix:
        if char not in  ['+','-','*','/','(',')', '^']:
            postfix += char
        if char == ')':
            while peak(stack) != '(':
                postfix += peak(stack)
                stack = pop(stack)
            stack = pop(stack)
        if char == '^' or char == '(':
            stack += char
        if (char in ['+', '-', '*', '/']) and precedence(peak(stack)) < precedence(char):
            stack += char
        if (char in ['+', '-', '*', '/']) and precedence(peak(stack)) > precedence(char):
            postfix += peak(stack)
            stack = pop(stack)
            stack += char
    return postfix

for i in range(int(input())):
    print(rpn(input()))
