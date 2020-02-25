class MaxHeap():
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
  
        while i != 0 and self.heapList[self.parent(i)] < self.heapList[i]:
            self.heapList[self.parent(i)], self.heapList[i] = self.heapList[i], self.heapList[self.parent(i)]
            i = self.parent(i); 

    def increaseKey(self, i, new_val): 
        self.heapList[i] = new_val; 
        while i != 0 and self.heapList[self.parent(i)] < self.heapList[i]:
            self.heapList[self.parent(i)], self.heapList[i] = self.heapList[i], self.heapList[self.parent(i)]
            i = self.parent(i);  
    
    def deleteKey(self, i):
        self.increaseKey(i, float("inf"))
        self.extractMax()

    def extractMax(self):
        if self.size <= 0:
            return -float("inf")
        if self.size == 1:
            self.size -= 1
            return self.heapList[0]
        root = self.heapList[0]; 
        self.heapList[0] = self.heapList[self.size-1]
        self.size -= 1
        self.MaxHeapify(0);   
        return root
    
    def MaxHeapify(self, i):
        l = self.leftChild(i); 
        r = self.rightChild(i); 
        largest = i; 
        if l < self.size and self.heapList[l] > self.heapList[largest]: 
            largest = l
        if r < self.size and self.heapList[r] > self.heapList[largest]:
            largest = r
        if largest != i:
            self.heapList[largest], self.heapList[i] = self.heapList[i], self.heapList[largest]
            self.MaxHeapify(largest)

    def findMin(self):
        Min = float("inf")
        for i in range((self.size+ 1)//2, self.size):
            if(self.heapList[i] < Min):
                Min = self.heapList[i]
        return Min

if __name__ == "__main__"    :
    heap = MaxHeap() 
    heap.insertKey(3) 
    heap.insertKey(2)  
    heap.insertKey(15) 
    heap.insertKey(5) 
    heap.insertKey(4) 
    heap.insertKey(45) 
    print(heap)
    heap.deleteKey(1)
    print(heap)
    print(f"Minimum Element: {heap.findMin()}")