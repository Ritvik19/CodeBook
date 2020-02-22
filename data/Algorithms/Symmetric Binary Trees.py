from BinaryTree import Node

def areMirrors(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    return root1.data == root2.data and areMirrors(root1.left, root2.right) and areMirrors(root1.right, root2.left)

if __name__ == "__main__":
    root1 = Node(1)
    root2 = Node(1)

    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)
    root1.left.right = Node(5)

    root2.left = Node(3)
    root2.right = Node(2)
    root2.right.left = Node(5)
    root2.right.right = Node(4)
    print("Inorder (Tree1):")
    print(*root1.inorderTraversal(root1))
    print("Inorder (Tree2):")
    print(*root2.inorderTraversal(root2))
    print(areMirrors(root1, root2))
