class Node:
    
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()

    def inorderTraversal(self, node):
        res = []
        if node:
            res = self.inorderTraversal(node.left)
            res.append(node.data)
            res = res + self.inorderTraversal(node.right)
        return res

    def preorderTraversal(self, node):
        res = []
        if node:
            res.append(node.data)
            res = res + self.preorderTraversal(node.left)
            res = res + self.preorderTraversal(node.right)
        return res
    
    def postorderTraversal(self, node):
        res = []
        if node:
            res = self.postorderTraversal(node.left)
            res = res + self.postorderTraversal(node.right)
            res.append(node.data)
        return res
    
    def __str__(self):
        return f"{self.data}"

if __name__ == "__main__":
    root = Node(27)
    root.left = Node(14)
    root.right = Node(35)
    root.left.left = Node(10)
    root.left.right = Node(19)
    root.right.left = Node(31)
    root.right.right = Node(42)
    print("Inorder:")
    print(*root.inorderTraversal(root))
    print("Preorder:")
    print(*root.preorderTraversal(root))
    print("Postorder:")
    print(*root.postorderTraversal(root))
