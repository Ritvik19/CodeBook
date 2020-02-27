class Vertex():
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        self.distance = float("inf")
        self.visited = False
        self.previous = None
        
    def addNeighbour(self, neighbour, weight=0):
        self.adjacent[neighbour] = weight

    def getConnections(self):
        return self.adjacent.keys()
    
    def getVertexID(self):
        return self.id
    
    def getWeight(self, neighbour):
        return self.adjacent[neighbour]
    
    def setDistance(self, dist):
        self.distance = dist
        
    def getDistance(self):
        return self.distance
    
    def setPrevious(self, prev):
        self.previous = prev
        
    def setVisited(self):
        self.visited = True
        
    def __str__(self)        :
        return f"{self.id}"
    
class Graph():
    def __init__(self):
        self.vertDictionary = {}
        self.numVertices = 0
        
    def __iter__(self):
        return iter(self.vertDictionary.values())
    
    def addVertex(self, node):
        self.numVertices += 1
        newVertex = Vertex(node)
        self.vertDictionary[node] = newVertex
        return newVertex
    
    def getVertex(self, n):
        if n in self.vertDictionary.keys():
            return self.vertDictionary[n]
        return None
    
    def getVertices(self):
        return self.vertDictionary.keys()
    
    def addEdge(self, frm, to, cost=0):
        if frm not in self.vertDictionary.keys():
            self.addVertex(frm)
        if to not in self.vertDictionary.keys():
            self.addVertex(to)
        self.vertDictionary[frm].addNeighbour(self.vertDictionary[to], cost)
        self.vertDictionary[to].addNeighbour(self.vertDictionary[frm], cost)
        
    def getEdges(self):
        edges = []
        for v in G:
            vid = v.getVertexID()
            for w in v.getConnections():
                wid = w.getVertexID()
                edges.append((vid, wid, v.getWeight(w)))
        return edges

if __name__ == "__main__":
    G = Graph()
    for a in ['a', 'b', 'c', 'd', 'e']:
        G.addVertex(a)
    G.addEdge('a', 'b', 4)
    G.addEdge('a', 'c', 1)
    G.addEdge('c', 'b', 2)
    G.addEdge('b', 'e', 4)
    G.addEdge('c', 'd', 3)
    G.addEdge('d', 'e', 5)
    print('Edges:')
    print(*G.getEdges(), sep="\n")