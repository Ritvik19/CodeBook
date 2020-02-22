from BinaryTree import Node


def height(root, ans):
    if (root == None):
        return 0
    left_height = height(root.left, ans)
    right_height = height(root.right, ans)
    ans[0] = max(ans[0], 1 + left_height + right_height)
    return 1 + max(left_height, right_height)

def diameter(root):
    if (root == None):
        return 0
    ans = [-999999999999]
    height_of_tree = height(root, ans)
    return ans[0]

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
