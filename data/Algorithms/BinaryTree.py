class Node:
    
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
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

if __name__ == "__main__":
    root = Node(27)
    root.insert(14)
    root.insert(35)
    root.insert(10)
    root.insert(19)
    root.insert(31)
    root.insert(42)
    print("Inorder:")
    print(*root.inorderTraversal(root))
    print("Preorder:")
    print(*root.preorderTraversal(root))
    print("Postorder:")
    print(*root.postorderTraversal(root))
