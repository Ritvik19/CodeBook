from BinaryTree import Node

def getMirror(node):
    if node is None:
        return
    else:
        getMirror(node.left)
        getMirror(node.right)
        temp = node.left
        node.left = node.right
        node.right = temp

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
    getMirror(root)
    print("Inorder (Mirror):")
    print(*root.inorderTraversal(root))
