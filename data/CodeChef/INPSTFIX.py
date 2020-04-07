prio = {'^':5, '*':4,'/':4,'+':3,'-':3,'(':2,')':1}

def topostfix(infix_src):
    postfix = list()
    stack = list()
    for x in ( infix_src ):
        if x.isalpha():
            postfix.append(x)
        if x in '+-*/^':
            while len( stack ) and prio[x] <= prio[ stack[-1]]:
                postfix.append( stack.pop() )
            stack.append(x)
        if x == '(':
            stack.append(x)
        if x == ')':
            while stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()

    while len(stack):
        if(stack[-1] == "("):
            stack.pop()
        else:
            postfix.append( stack.pop() )

    return postfix

for _ in range(int(input()))    :
    lens = int(input())
    expr = input()
    print("".join(topostfix(expr)))