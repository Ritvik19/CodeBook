class Vertex():
    def __init__(self, node):
        self.id = node
        self.visited = False
        
    def __str__(self):
        return f"{self.id}"
    
    def addNeighbour(self, neighbour, G):
        G.addEdge(self.id, neighbour)
        
    def getConnections(self, G):
        return G.adjMatrix[self.id]
    
    def getVertexID(self):
        return self.id
    
    def setVertexID(self, newID):
        self.id = newID
        
    def setVisited(self):
        self.visited = True
        
class Graph():
    def __init__(self, numVertices, cost=0):
        self.adjMatrix = [[-1 for _ in range(numVertices)] for _ in range(numVertices)]
        for i in range(numVertices):
            self.adjMatrix[i][i] = cost
        self.numVertices = numVertices
        self.vertices = [Vertex(i) for i in range(numVertices)]
        
    def setVertex(self, vtx, newID):
        if 0 <= vtx < self.numVertices:
            self.vertices[vtx].setVertexID(newID)
            
    def getVertex(self, n):
        for vtx in range(self.numVertices):
            if self.vertices[vtx].getVertexID() == n:
                return vtx
        return -1
        
    def addEdge(self, frm, to, cost=0):
        f = self.getVertex(frm)
        t = self.getVertex(to)
        if f != -1 and t != -1:
            self.adjMatrix[f][t] = cost
            self.adjMatrix[t][f] = cost
            
    def getVertices(self):
        return [x.getVertexID() for x in self.vertices]
        
    def printMatrix(self):
        for _ in self.adjMatrix:
            print(*_)
    
    def getEdges(self):
        edges = []
        for v in range(self.numVertices):
            for u in range(self.numVertices):
                if self.adjMatrix[u][v] != -1:
                    vid = self.vertices[v].getVertexID()
                    uid = self.vertices[u].getVertexID()
                    edges.append((vid, uid, self.adjMatrix[v][u]))
        return edges
    
if __name__ == "__main__"    :
    G = Graph(5)
    for i, a in enumerate(['a','b','c','d','e']):
        G.setVertex(i, a)
    G.addEdge('a', 'e', 10)
    G.addEdge('a', 'c', 20)
    G.addEdge('c', 'b', 30)
    G.addEdge('e', 'd', 40)
    G.addEdge('f', 'e', 50)
    print('Adjacency Matrix:')
    G.printMatrix()
    print('Edges:')
    print(*G.getEdges(), sep="\n")