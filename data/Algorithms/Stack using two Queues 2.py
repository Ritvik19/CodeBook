from Queue import Queue

class Stack:
    def __init__(self, limit):
        self.q1 = Queue(limit)
        self.q2 = Queue(limit)
        self.limit = limit
        self.curr_size = 0

    def push(self, x):
        self.curr_size += 1
        self.q1.enqueue(x)

    def pop_(self):
        if (self.q1.isEmpty()):
            print("Stack Underflow")
            return
        self.curr_size -= 1
        while self.q1.size > 1:
            self.q2.enqueue(self.q1.dequeue())
        elem = self.q1.dequeue()
        # swap the names of two queues
        self.q1, self.q2 = self.q2, self.q1
        return elem

    def size(self):
        return self.curr_size

    def display(self):
        print("Stack:")
        for elem in self.q1.queue[::-1]:
            print("\t", elem)

if __name__ == '__main__':
    stack = Stack(3)
    print("POP called:", end="\n\t")
    stack.pop_()
    stack.push(5)
    stack.push(4)
    stack.push(3)
    stack.display()
    print('POP: ', stack.pop_())
    stack.display()
