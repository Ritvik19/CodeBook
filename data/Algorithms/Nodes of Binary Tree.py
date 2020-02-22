from BinaryTree import Node

def fullNodes(root):
    if root == None:
        return 0
    res = 0
    if root.left and root.right:
        res += 1
    res += fullNodes(root.left) + fullNodes(root.right)
    return res

def halfNodes(root):
    if root == None:
        return 0
    res = 0
    if root.left or root.right:
        res += 1
    res += halfNodes(root.left) + halfNodes(root.right)
    return res

def leafNodes(root):
    if root == None:
        return 0
    res = 0
    if not (root.left or root.right):
        res += 1
    res += leafNodes(root.left) + leafNodes(root.right)
    return res

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
    print(f"Full Nodes: {fullNodes(root)}")
    print(f"Half Nodes: {halfNodes(root)}")
    print(f"Leaf Nodes: {leafNodes(root)}")
