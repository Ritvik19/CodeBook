from Stack import Stack
import sys
import os

def blockPrint():
    sys.stdout = open(os.devnull, 'w')

def enablePrint():
    sys.stdout = sys.__stdout__

def postfixEval(string):
    opStack = Stack(len(string))
    tokenList = string.split()
    for token in tokenList:
        if token in "0123456789":
            blockPrint()
            opStack.push(token)
            enablePrint()
        else:
            op2 = opStack.pop_()
            op1 = opStack.pop_()
            result = doMath(token, op1, op2)
            blockPrint()
            opStack.push(result)
            enablePrint()
    return opStack.pop_()

def doMath(op, op1, op2):
    return eval(f"{op1}{op}{op2}")

if __name__ == '__main__':
    print(postfixEval('1 2 * 3 4 * +'))
