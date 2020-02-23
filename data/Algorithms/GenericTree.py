class Node():
    def __init__(self, data):
        self.data = data
        self.firstChild = None
        self.nextSibling = None
    
    def getFirstChild(self):
        return self.firstChild
    
    def setFirstChild(self, firstChild):
        self.firstChild = firstChild
        
    def getNextSibling(self):
        return self.nextSibling
    
    def setNextSibling(self, nextSibling):
        self.nextSibling = nextSibling
    
    def __str__(self):
        return f"{self.data}"

def siblingsCount(node):
    count = 0
    while(node):
        count += 1
        node = node.getNextSibling()
    return count

def childrenCount(node):
    count = 0
    node = node.getFirstChild()
    while(node):
        count += 1
        node = node.getNextSibling()
    return count

def depth(node):
    if node is None:
        return 0
    return max(depth(node.getFirstChild())+1, depth(node.getNextSibling()))

def treeSum(root):
    if root is None:
        return 0
    return root.data + treeSum(root.getFirstChild()) + treeSum(root.getNextSibling())
    
if __name__ == "__main__":
    root = Node(1)
    
    root.setFirstChild(Node(2))
    root.getFirstChild().setNextSibling(Node(3))
    root.getFirstChild().getNextSibling().setNextSibling(Node(4))
    
    root.getFirstChild().setFirstChild(Node(5))
    root.getFirstChild().getFirstChild().setNextSibling(Node(6))
    root.getFirstChild().getFirstChild().getNextSibling().setNextSibling(Node(7))
    
    root.getFirstChild().getNextSibling().setFirstChild(Node(8))
    root.getFirstChild().getNextSibling().getFirstChild().setNextSibling(Node(9))
    root.getFirstChild().getNextSibling().getFirstChild().getNextSibling().setNextSibling(Node(10))
    
    root.getFirstChild().getNextSibling().getNextSibling().setFirstChild(Node(11))
    root.getFirstChild().getNextSibling().getNextSibling().getFirstChild().setNextSibling(Node(12))
    root.getFirstChild().getNextSibling().getNextSibling().getFirstChild().getNextSibling().setNextSibling(Node(13))

    print(f"Child of root element: {childrenCount(root)}")
    print(f"Siblings of first child of root element: {siblingsCount(root.getFirstChild())}")
    print(f"Depth: {depth(root)}")
