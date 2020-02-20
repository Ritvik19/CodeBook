from Queue import Queue
from Stack import Stack

import sys
import os


def blockPrint():
    sys.stdout = open(os.devnull, 'w')


def enablePrint():
    sys.stdout = sys.__stdout__

def checkStackPermutation(ip, op):
    tempStack = Stack(ip.size)
    while (not ip.isEmpty()):
        ele = ip.dequeue()
        if (ele == op.peek()):
            op.dequeue()
            while not tempStack.isEmpty():
                if (tempStack.top() == op.peek()):
                    tempStack.pop_()
                    op.dequeue()
                else:
                    break
        else:
            blockPrint()
            tempStack.push(ele)
            enablePrint()

    return (ip.isEmpty() and tempStack.isEmpty())


if __name__ == '__main__':
    ip = Queue(3)
    ip.enqueue(1)
    ip.enqueue(2)
    ip.enqueue(3)
    op = Queue(3)
    op.enqueue(2)
    op.enqueue(1)
    op.enqueue(3)
    print(checkStackPermutation(ip, op))
