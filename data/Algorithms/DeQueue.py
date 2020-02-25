class DeQueue():
    def __init__(self):
        self.queue = []
        self.size = 0
        
    def isEmpty(self):
        return self.size == 0
    
    def enqueueRear(self, data):
        self.queue.append(data)    
        self.size += 1

    def enqueueFront(self, data):
        self.queue.insert(0, data)    
        self.size += 1 
        
    def dequeueFront(self):
        e = self.queue.pop(0)
        self.size -= 1
        return e

    def dequeueRear(self):
        e = self.queue.pop(-1)
        self.size -= 1
        return e
    
    def peakRear(self):
        return self.queue[-1]
    
    def peakFront(self):
        return self.queue[0]
    
    def display(self):
        print(*self.queue, sep=' <- ')
        
    def clear(self):
        self.queue = []
        self.size = 0
        
if __name__ == "__main__":
    dequeue = DeQueue()
    dequeue.enqueueFront(3)
    dequeue.enqueueFront(2)
    dequeue.enqueueFront(1)
    dequeue.display()
    dequeue.enqueueRear(4)
    dequeue.enqueueRear(5)
    dequeue.display()
    dequeue.dequeueFront()
    dequeue.display()
    dequeue.dequeueRear()
    dequeue.display()
