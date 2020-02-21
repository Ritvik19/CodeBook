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
    root.insert(14)
    root.insert(35)
    root.insert(10)
    root.insert(19)
    root.insert(31)
    root.insert(42)
    root.insert(45)
    print("Inorder:")
    print(*root.inorderTraversal(root))
    print(f"Full Nodes: {fullNodes(root)}")
    print(f"Half Nodes: {halfNodes(root)}")
    print(f"Leaf Nodes: {leafNodes(root)}")
