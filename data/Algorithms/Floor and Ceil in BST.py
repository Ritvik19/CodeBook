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


def floorBST(root, data):
    if root is None:
        return float('inf')
    if root.data == data:
        return root.data
    if data < root.data:
        return floorBST(root.left, data)
    floor = floorBST(root.right, data)
    if floor <= data:
        return floor
    else:
        return root.data


def ceilBST(root, data):
    if root is None:
        return -float('inf')
    if root.data == data:
        return root.data
    if data > root.data:
        return ceilBST(root.right, data)
    ceil = ceilBST(root.left, data)
    if ceil >= data:
        return ceil
    else:
        return root.data


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
    print(f"Floor of 45: {floorBST(root, 45)}")
    print(f"Ceil of 45: {ceilBST(root, 45)}")
