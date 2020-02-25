class PriorityQueue(object): 
    def __init__(self): 
        self.queue = [] 
  
    def __str__(self): 
        return ' '.join([str(i) for i in self.queue]) 
  
    def isEmpty(self): 
        return len(self.queue) == [] 
   
    def insert(self, data): 
        self.queue.append(data) 
  
    def delete(self): 
        try: 
            max = 0
            for i in range(len(self.queue)): 
                if self.queue[i] > self.queue[max]: 
                    max = i 
            item = self.queue[max] 
            del self.queue[max] 
            return item 
        except IndexError: 
            return None 
        
    def peek(self): 
        try: 
            max = 0
            for i in range(len(self.queue)): 
                if self.queue[i] > self.queue[max]: 
                    max = i 
            return self.queue[max] 
        except IndexError: 
            return None 
  
if __name__ == '__main__': 
    pQueue = PriorityQueue() 
    pQueue.insert(12) 
    pQueue.insert(1) 
    pQueue.insert(14) 
    pQueue.insert(7) 
    print(pQueue)              
    print(f"Item Deleted: {pQueue.delete()}") 
    print(pQueue)
    print(f"Item Peeked: {pQueue.peek()}") 
    print(pQueue)