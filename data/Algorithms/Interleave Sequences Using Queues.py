from Queue import Queue


def interleaveSequence(q):
    n = q.size
    q1 = Queue(n)
    q2 = Queue(n)
    
    for i in range(n//2):
        q1.enqueue(q.dequeue())
    
    for i in range(n//2):
        q2.enqueue(q.dequeue())
        
    for i in range(n//2):
        q.enqueue(q1.dequeue())
        q.enqueue(q2.dequeue())


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
