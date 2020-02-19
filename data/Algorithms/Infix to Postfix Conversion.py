from Stack import Stack
import sys
import os


def blockPrint():
    sys.stdout = open(os.devnull, 'w')


def enablePrint():
    sys.stdout = sys.__stdout__

prec = {
    '*': 3,
    '/': 3,
    '+': 2,
    '-': 2,
    '(': 1
}

def infixToPostfix(string):
    opStack = Stack(len(string))
    postfixList = []
    tokenList = string.split()
    
    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
            postfixList.append(token)
        elif token == '(':
            blockPrint()
            opStack.push(token)
            enablePrint()
        elif  token == ')':
            topToken = opStack.pop_()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop_()
        else:
            while (not opStack.isEmpty()) and (prec[opStack.top()] >= prec[token]):
                postfixList.append(opStack.pop_())
            blockPrint()
            opStack.push(token)
            enablePrint()
    while not opStack.isEmpty():
        postfixList.append(opStack.pop_())
    return " ".join(postfixList)


if __name__ == '__main__':
    print(infixToPostfix('A * B + C * D'))
