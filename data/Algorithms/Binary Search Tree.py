class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def __str__(self):
        return f"{self.data}"
        
def find(root, data):
    currentNode = root
    while currentNode is not None and data != currentNode.data:
        if data> currentNode.data:
            currentNode = currentNode.right
        else:
            currentNode = currentNode.left
    return currentNode

def findMin(root):
    currentNode = root
    if currentNode.left is None:
        return currentNode
    else:
        return findMin(currentNode.left)
    
def findMax(root):
    currentNode = root
    if currentNode.right is None:
        return currentNode
    else:
        return findMax(currentNode.right)
    
def successorBST(root):
    currentNode = None
    if root.right is not None:
        currentNode = root.right
        while currentNode.left is not None:
            currentNode = currentNode.left
    return currentNode

def predecessorBST(root):
    currentNode = None
    if root.left is not None:
        currentNode = root.left
        while currentNode.right is not None:
            currentNode = currentNode.right
    return currentNode

def insert(node, key): 
    if node is None: 
        return Node(key) 
    if key < node.data: 
        node.left = insert(node.left, key) 
    else: 
        node.right = insert(node.right, key) 
    return node 

def inorderTraversal(node):
    res = []
    if node:
        res = inorderTraversal(node.left)
        res.append(node.data)
        res = res + inorderTraversal(node.right)
    return res

def preorderTraversal(node):
    res = []
    if node:
        res.append(node.data)
        res = res + preorderTraversal(node.left)
        res = res + preorderTraversal(node.right)
    return res

def postorderTraversal(node):
    res = []
    if node:
        res = postorderTraversal(node.left)
        res = res + postorderTraversal(node.right)
        res.append(node.data)
    return res

def deleteNode(root, key): 
    if root is None: 
        return root   
    if key < root.data: 
        root.left = deleteNode(root.left, key)  
    elif(key > root.data): 
        root.right = deleteNode(root.right, key) 
    else: 
        if root.left is None : 
            temp = root.right  
            root = None 
            return temp    
        elif root.right is None : 
            temp = root.left  
            root = None
            return temp 
        temp = findMin(root.right)   
        root.data = temp.data  
        root.right = deleteNode(root.right , temp.data) 
    return root  

if __name__ == "__main__":
    root = Node(10)
    root = insert(root, 50) 
    root = insert(root, 30) 
    root = insert(root, 20) 
    root = insert(root, 40) 
    root = insert(root, 70) 
    root = insert(root, 60) 
    root = insert(root, 80)
    print(inorderTraversal(root))
    root = deleteNode(root, 20) 
    print(inorderTraversal(root))