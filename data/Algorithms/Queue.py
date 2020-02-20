class Queue():
    def __init__(self, limit):
        self.queue = []
        self.limit = limit
        self.front = -1
        self.rear = -1
        self.size = 0
        
    def isEmpty(self):
        return self.size == 0
    
    def isFull(self):
        return self.size == self.limit
    
    def enqueue(self, data):
        if self.isFull():
            print("Queue Overflow!")
            return
        self.queue.append(data)    
        
        if self.front == -1:
            self.front = 0
            self.rear = 0
        else:
            self.rear = self.size
        self.size += 1
        
    def dequeue(self):
        if self.isEmpty():
            print("Queue Underflow!")
            return
        element = self.queue.pop(0)
        self.size -= 1
        if self.size == 0:
            self.front = -1
            self.rear = -1
        else:
            self.rear = self.size -1
        return element
        
    def peek(self):
        if self.isEmpty():
            print("Queue Underflow!")
            return
        return self.queue[0]
        
        
    def display(self):
        print(*self.queue, sep=' <- ')
        
    def clear(self):
        self.queue = []
        self.front = -1
        self.rear = -1
        self.size = 0
        
if __name__ == "__main__":
    queue = Queue(3)
    print("Remove an element from initially empty queue")
    print("Adding elements")
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.display())
    print("Add another element")
    queue.enqueue(4)
    queue.dequeue()
    print(queue.display())
