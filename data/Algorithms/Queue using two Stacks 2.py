import sys
import os

from Stack import Stack

def blockPrint():
    sys.stdout = open(os.devnull, 'w')

def enablePrint():
    sys.stdout = sys.__stdout__

class Queue:
    def __init__(self, limit):
        self.s1 = Stack(limit)
        self.s2 = Stack(limit)
        self.limit = limit

    def enqueue(self, x):
        blockPrint()
        self.s1.push(x)
        enablePrint()

    def dequeue(self):
        if self.s1.isEmpty() and self.s2.isEmpty():
            print("Queue Underflow!")
            return
        if self.s2.isEmpty():
            while not self.s1.isEmpty():
                blockPrint()
                self.s2.push(self.s1.pop_())
                enablePrint()
        return self.s2.pop_()

if __name__ == "__main__":
    queue = Queue(3)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print("Enqueued: 1, 2, 3")
    print("Dequeue:")
    print(queue.dequeue())
