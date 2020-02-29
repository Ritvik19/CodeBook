class DisjointSet():
    def __init__(self, n):
        self.data = [i for i in range(n)]
        
    def find(self, i):
        if i != self.data[i]:
            self.data[i] = self.find(self.data[i])
        return self.data[i]
        
    def union(self, i, j):
        pi, pj = self.find(i), self.find(j)
        if pi != pj:
            self.data[pi] = pj
            
    def connected(self, i, j):
        return self.find(i) == self.find(j)
        
if __name__ == '__main__':
    n = 10
    s = DisjointSet(n)
    connections = [(0, 1), (1, 2), (0, 9), (5, 6), (6, 4), (5, 9)]
    for i, j in connections:
        s.union(i, j)
    for i in range(n):
        print('item', i, '-> component', s.find(i))