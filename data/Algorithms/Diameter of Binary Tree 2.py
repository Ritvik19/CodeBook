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
