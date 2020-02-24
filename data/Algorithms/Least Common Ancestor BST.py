class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def __str__(self):
        return f"{self.data}"

def insert(node, key): 
    if node is None: 
        return Node(key) 
    if key < node.data: 
        node.left = insert(node.left, key) 
    else: 
        node.right = insert(node.right, key) 
    return node 

def lca(root, n1, n2): 
    if root is None: 
        return None
  
    if(root.data > n1 and root.data > n2): 
        return lca(root.left, n1, n2) 

    if(root.data < n1 and root.data < n2): 
        return lca(root.right, n1, n2) 
  
    return root

def inorderTraversal(node):
    res = []
    if node:
        res = inorderTraversal(node.left)
        res.append(node.data)
        res = res + inorderTraversal(node.right)
    return res
            
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
    print(f"Least Common Ancestor of 50 and 30: {lca(root, 50, 30)}")