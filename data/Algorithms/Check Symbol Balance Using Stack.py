from Stack import Stack
import sys
import os


def blockPrint():
    sys.stdout = open(os.devnull, 'w')


def enablePrint():
    sys.stdout = sys.__stdout__


def checkSymbolBalance(string):
    stack_ = Stack(len(string))
    for s in string:
        if s in ['(', '{', '[']:
            blockPrint()
            stack_.push(s)
            enablePrint()
        elif s in [')', '}', ']']:
            s_ = stack_.pop_()
            if (s_, s) not in [('(', ')'), ('{', '}'), ('[', ']')]:
                return False
        else:
            pass
    return stack_.isEmpty()


if __name__ == '__main__':
    print(checkSymbolBalance('(({}({{}})))'))
