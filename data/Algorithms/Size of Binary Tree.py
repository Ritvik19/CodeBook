from BinaryTree import Node

def sizeBinaryTree(root):
    if root is None:
        return 0
    return sizeBinaryTree(root.left) + sizeBinaryTree(root.right) + 1

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
    print(f"Size: {sizeBinaryTree(root)}")
