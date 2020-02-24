class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return f"{self.data}"


def insert(node, key):
    if node is None:
        return Node(key)
    if key < node.data:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node


def inorderTraversal(node):
    res = []
    if node:
        res = inorderTraversal(node.left)
        res.append(node.data)
        res = res + inorderTraversal(node.right)
    return res


def removeOutsideRange(root, Min, Max):
    if root == None:
        return None

    root.left = removeOutsideRange(root.left, Min, Max)
    root.right = removeOutsideRange(root.right, Min, Max)

    if root.data < Min:
        rChild = root.right
        return rChild

    if root.data > Max:
        lChild = root.left
        return lChild

    return root


if __name__ == "__main__":
    root = Node(10)
    root = insert(root, 50)
    root = insert(root, 30)
    root = insert(root, 20)
    root = insert(root, 40)
    root = insert(root, 70)
    root = insert(root, 60)
    root = insert(root, 80)
    print(*inorderTraversal(root))
    root = removeOutsideRange(root, 30, 60)
    print("Inorder traversal of the modified tree is:")
    print(*inorderTraversal(root))
