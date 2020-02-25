class MinHeap():
    def __init__ (self):
        self.heapList = []
        self.size = 0
        
    def __str__(self):
        return ' '.join([str(x) for x in self.heapList])
    
    def parent(self, index):
        return index//2
    
    def leftChild(self, index):
        return index*2 + 1
    
    def rightChild(self, index):
        return index*2 + 2
    
    def insertKey(self, k):
        self.size += 1 
        i = self.size - 1
        self.heapList.append(k)
  
        while i != 0 and self.heapList[self.parent(i)] > self.heapList[i]:
            self.heapList[self.parent(i)], self.heapList[i] = self.heapList[i], self.heapList[self.parent(i)]
            i = self.parent(i); 

    def decreaseKey(self, i, new_val): 
        self.heapList[i] = new_val; 
        while i != 0 and self.heapList[self.parent(i)] > self.heapList[i]:
            self.heapList[self.parent(i)], self.heapList[i] = self.heapList[i], self.heapList[self.parent(i)]
            i = self.parent(i);  
    
    def deleteKey(self, i):
        self.decreaseKey(i, -float("inf"))
        self.extractMin()

    def extractMin(self):
        if self.size <= 0:
            return float("inf")
        if self.size == 1:
            self.size -= 1
            return self.heapList[0]
        root = self.heapList[0]; 
        self.heapList[0] = self.heapList[self.size-1]
        self.size -= 1
        self.MinHeapify(0);   
        return root
    
    def MinHeapify(self, i):
        l = self.leftChild(i); 
        r = self.rightChild(i); 
        smallest = i; 
        if l < self.size and self.heapList[l] < self.heapList[smallest]: 
            smallest = l
        if r < self.size and self.heapList[r] < self.heapList[smallest]:
            smallest = r
        if smallest != i:
            self.heapList[smallest], self.heapList[i] = self.heapList[i], self.heapList[smallest]
            self.MinHeapify(smallest)

    def findMax(self):
        Max= -float("inf")
        for i in range((self.size+ 1)//2, self.size):
            if(self.heapList[i] > Max):
                Max = self.heapList[i]
        return Max

if __name__ == "__main__"    :
    heap = MinHeap() 
    heap.insertKey(3) 
    heap.insertKey(2)  
    heap.insertKey(15) 
    heap.insertKey(5) 
    heap.insertKey(4) 
    heap.insertKey(45) 
    print(heap)
    heap.deleteKey(1)
    print(heap)
    print(f"Maximum Element: {heap.findMax()}")