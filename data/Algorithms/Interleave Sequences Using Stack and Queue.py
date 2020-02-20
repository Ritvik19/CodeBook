from Stack import Stack
from Queue import Queue

import sys
import os

def blockPrint():
    sys.stdout = open(os.devnull, 'w')

def enablePrint():
    sys.stdout = sys.__stdout__

def interleaveSequence(q): 
    if (q.size % 2 != 0):  
        print("Input even number of integers.") 
        return
    
    halfSize = q.size // 2  
    s = Stack(halfSize) 
    
    for i in range(halfSize): 
        blockPrint()
        s.push(q.dequeue())
        enablePrint()

    while not s.isEmpty():  
        q.enqueue(s.pop_())  

    for i in range(halfSize): 
        q.enqueue(q.dequeue())  

    for i in range(halfSize): 
        blockPrint()
        s.push(q.dequeue())
        enablePrint()

    while not s.isEmpty():
        q.enqueue(s.pop_())  
        q.enqueue(q.dequeue())

if __name__ == '__main__': 
    q = Queue(10) 
    q.enqueue(11)  
    q.enqueue(12)  
    q.enqueue(13)  
    q.enqueue(14)  
    q.enqueue(15)  
    q.enqueue(16)  
    q.enqueue(17)  
    q.enqueue(18)  
    q.enqueue(19)  
    q.enqueue(20)  
    q.display()
    print("Interleaving")
    interleaveSequence(q)
    q.display()
