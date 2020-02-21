from BinaryTree import Node

def depthBinaryTree(root):
    if root is None:
        return 0
    return max(depthBinaryTree(root.left), depthBinaryTree(root.right)) + 1

if __name__ == "__main__":
    root = Node(27)
    root.insert(14)
    root.insert(35)
    root.insert(10)
    root.insert(19)
    root.insert(31)
    root.insert(42)
    root.insert(45)
    print("Inorder:")
    print(*root.inorderTraversal(root))
    print(f"Depth: {depthBinaryTree(root)}")
