from BinaryTree import Node

def leastCommonAncestor(root, alpha, beta):
    if root is None:
        return None
    if root.data == alpha or root.data == beta:
        return root
    
    left = leastCommonAncestor(root.left, alpha, beta)
    right = leastCommonAncestor(root.right, alpha, beta)
    
    if left and right:
        return root
    else:
        return left if left else right

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
    print(f"LCA of 35 and 45: {leastCommonAncestor(root, 45, 35)}")
