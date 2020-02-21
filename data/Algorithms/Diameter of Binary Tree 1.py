from BinaryTree import Node


def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))

def diameter(root):
    if root is None:
        return 0
    lheight = height(root.left)
    rheight = height(root.right)
    ldiameter = diameter(root.left)
    rdiameter = diameter(root.right)
    return max(lheight + rheight + 1, max(ldiameter, rdiameter))

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
    print(f"Diameter: {diameter(root)}")