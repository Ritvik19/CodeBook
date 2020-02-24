class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def __str__(self):
        return f"{self.data}"
    
def sortedArrayToBST(arr): 
    if not arr: 
        return None
    mid = len(arr) // 2
    root = Node(arr[mid]) 
    root.left = sortedArrayToBST(arr[:mid]) 
    root.right = sortedArrayToBST(arr[mid+1:]) 
    return root 
  
def preorderTraversal(node):
    res = []
    if node:
        res.append(node.data)
        res = res + preorderTraversal(node.left)
        res = res + preorderTraversal(node.right)
    return res 
  
if __name__ == "__main__"  :
    arr = [1, 2, 3, 4, 5, 6, 7] 
    root = sortedArrayToBST(arr) 
    print ("PreOrder Traversal of constructed BST:") 
    print(*preorderTraversal(root) )