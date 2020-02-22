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
    root.left = Node(14)
    root.right = Node(35)
    root.left.left = Node(10)
    root.left.right = Node(19)
    root.right.left = Node(31)
    root.right.right = Node(42)
    root.left.left.left = Node(45)
    print("Inorder:")
    print(*root.inorderTraversal(root))
    print(f"Diameter: {diameter(root)}")
