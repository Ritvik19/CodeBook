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


def rangePrinter(root, k1, k2):
    if root is None:
        return
    if k1 < root.data:
        rangePrinter(root.left, k1, k2)
    if k1 <= root.data and k2 >= root.data:
        print(root, end=" ")
    if k2 > root.data:
        rangePrinter(root.right, k1, k2)


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
    print("Elements between 30 and 60:")
    rangePrinter(root, 30, 60)
