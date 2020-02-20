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
        while not self.s1.isEmpty():
            blockPrint()
            self.s2.push(self.s1.pop_())
            enablePrint()

        blockPrint()
        self.s1.push(x)
        enablePrint()

        while not self.s2.isEmpty():
            blockPrint()
            self.s1.push(self.s2.pop_())
            enablePrint()

    def dequeue(self):
        if self.s1.isEmpty():
            print("Queue Underflow!")
            return
        return self.s1.pop_()

    def display(self):
        print(*self.s1.stack[::-1], sep=' <- ')


if __name__ == "__main__":
    queue = Queue(3)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.display()
    queue.dequeue()
    queue.enqueue(4)
    queue.display()
