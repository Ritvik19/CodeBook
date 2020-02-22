from BinaryTree import Node

def allAncestor(root, node):
    if root is None:
        return False

    if root.data == node:
        return True

    if allAncestor(root.left, node) or allAncestor(root.right, node):
        print (root.data)
        return True
    return False

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
    print("All Ancestors of 45:")
    allAncestor(root, 45)
