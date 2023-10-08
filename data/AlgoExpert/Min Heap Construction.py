class MinHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        first_parent_idx = (len(array) - 2) // 2
        for current_idx in reversed(range(first_parent_idx + 1)):
            self.siftDown(current_idx, len(array)-1, array)
        return array

    def siftDown(self, current_idx, end_idx, heap):
        child_one_idx = current_idx * 2 + 1
        while child_one_idx <= end_idx:
            child_two_idx = current_idx * 2 + 2 if current_idx * 2 + 2 <= end_idx else -1
            if child_two_idx != -1 and heap[child_two_idx] < heap[child_one_idx]:
                idx_to_swap = child_two_idx
            else: 
                idx_to_swap = child_one_idx
            if heap[idx_to_swap] < heap[current_idx]:
                self.swap(current_idx, idx_to_swap, heap)
                current_idx = idx_to_swap
                child_one_idx = current_idx * 2 + 1
            else:
                return

    def siftUp(self, current_idx):
        parent_idx = (current_idx - 1) // 2
        while current_idx > 0 and self.heap[current_idx] < self.heap[parent_idx]:
            self.swap(current_idx, parent_idx)
            current_idx = parent_idx
            parent_idx = (current_idx - 1) // 2

    def peek(self):
        return self.heap[0]

    def remove(self):
        self.swap(0, len(self.heap) - 1)
        val_to_remove = self.heap.pop()
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return val_to_remove

    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1)

    def swap(self, i, j, heap=None):
        if heap is None:
            heap = self.heap
        heap[i], heap[j] = heap[j], heap[i]
